#Criando funções de dependencia

#Bibliotecas
from modelagem_db import db
from sqlalchemy.orm import sessionmaker
from modelagem_db import Usuario
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException
from jose import jwt, JWTError
from main import SECRET_KEY, ALGORITHM, oauth2_schema

def pegar_sessao():
  #Abre uma sessão para carregar dados do banco de dados
  try:
    Session = sessionmaker(bind=db)
    session = Session()
    yield session #retorna o valor requerido do banco de dados seme ncerrar a sessão
  finally:
    #Em caso de erro do try, encerra a seção
    session.close()
    
def verificar_token(token: str = Depends(oauth2_schema), session: Session = Depends(pegar_sessao)):
  try:
      dic_info = jwt.decode(token, SECRET_KEY, ALGORITHM)
      usuario_id = dic_info.get("sub")
  except JWTError as error:
    print(error)
    raise HTTPException(status_code=401, detail="Acesso Negado, verifique a validade do token")
  #verificar validade de token
  #extrair id do token
  usuario = session.query(Usuario).filter(Usuario.id==usuario_id).first()
  if not usuario:
    raise HTTPException(status_code=401, detail="Acesso Inválido")
  return usuario

