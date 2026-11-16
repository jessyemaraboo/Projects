#Rota de login e autenticação

#Bibliotecas
from fastapi import APIRouter, Depends, HTTPException
from modelagem_db import Usuario
from dependencias import pegar_sessao, verificar_token
from main import bcrypt_context, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from fastapi.security import OAuth2PasswordRequestForm

#Prefixos de rotas
auth_router = APIRouter(prefix = "/auth", tags = ["auth"])

def criar_token(usuario_id, duracao_token = timedelta(minutes = ACCESS_TOKEN_EXPIRE_MINUTES)):
  #Token JWT
  #armazenar no noketn: id de usuario e data de expiração
  data_exp = datetime.now(timezone.utc) + duracao_token
  dic_info = {"sub": str(usuario_id), "exp": data_exp}
  encoded_jwt = jwt.encode(dic_info, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

  #token = f"fnsgaya47gfs7{usuario_id}"

def autenticar_usuario(email, senha, session):
  usuario = session.query(Usuario).filter(Usuario.email==email).first()
  if not usuario:
    return False
  elif not bcrypt_context.verify(senha, usuario.senha):
    return False
  return usuario

#Método GET
@auth_router.get("/")
async def home():
  return {"mensagem":"Rota de autenticação"}

#Gerenciamento de sessão

#Método POST
@auth_router.post("/criar-conta")
async def criar_conta(UsuarioSchema:UsuarioSchema, session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(pegar_sessao)):
  usuario = session.query(Usuario).filter(Usuario.email == UsuarioSchema.email).first()
  if usuario:
    #Já cadastrado
    raise HTTPException(status_code=400, detail="E-mail já cadastrado")
  else:
    senha_criptografada = bcrypt_context.hash(UsuarioSchema.senha)
    novo_usuario = Usuario(UsuarioSchema.nome, UsuarioSchema.email, senha_criptografada, UsuarioSchema.ativo, UsuarioSchema.admin)
    session.add(novo_usuario)
    session.commit()
    return {"mensagem": f"email {UsuarioSchema.email} cadastrado com sucesso!"}
  
"""
Rota de Login
login recebe email e senha gera um token JWT (Json Web token) que é uma sequencia de caracteres que serão isados para validação e autenticação.

"""
@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(pegar_sessao)):
  usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
  if not usuario:
    raise HTTPException(status_code=400, detail="Usuário não encontrado ou credenciais inválidas")
  else:
    access_token = criar_token(usuario.id)
    refresh_token = criar_token(usuario.id, duracao_token=timedelta(days=7))
    return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "Bearer"
            }

@auth_router.post("/login-form")
async def login_form(dados_formulario: OAuth2PasswordRequestForm = Depends(), session: Session = Depends(pegar_sessao)):
  usuario = autenticar_usuario(dados_formulario.username, dados_formulario.password, session)
  if not usuario:
    raise HTTPException(status_code=400, detail="Usuário não encontrado ou credenciais inválidas")
  else:
    access_token = criar_token(usuario.id)
    return {
            "access_token": access_token,
            "token_type": "Bearer"
            }

#Rota de token
@auth_router.get("/refresh")
async def refresh_token(usuario: Usuario = Depends(verificar_token)):
  #verificar token
  access_token = criar_token(usuario.id)
  return {
          "access_token": access_token,
          "token_type": "Bearer"
            }

#OAuth2