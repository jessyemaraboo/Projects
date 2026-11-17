#Base do aplicativo
#Bibliotecas
from fastapi import FastAPI
from passlib.context import CryptContext #Criptogafia de senhas
from dotenv import load_dotenv #Importa aquivos de uma pasta de ambiente .env
from fastapi.security import OAuth2PasswordBearer
import os

#Criptografia de senhas
load_dotenv()

#.env
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES= int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

#Criando criptografor de senhas
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_schema = OAuth2PasswordBearer(tokenUrl="auth/login-form")
#Aplicativo
app = FastAPI()

#Agregando rotas
from routes.auth_route import auth_router
from routes.order_route import order_router
from routes.admin_route import admin_router

app.include_router(auth_router)
app.include_router(order_router)
app.include_router(admin_router)


"""
Inicializando a interface da API
python -m uvicorn main: app --reload 
"""