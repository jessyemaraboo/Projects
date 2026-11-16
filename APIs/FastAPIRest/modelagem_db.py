#Modelagem de banco de dados

#Bibliotecas
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Float, ForeignKey, Enum
from enums import StatusPedido
from sqlalchemy.orm import declarative_base, Relationship
from sqlalchemy_utils.types import ChoiceType

#Conexão com o banco de dados
db = create_engine("sqlite:///banco.db")

#Base do banco de dados
Base = declarative_base()

#Tabelas
#Usuário
class Usuario(Base):
  __tablename__ = "usuario"
#Tabelas
  id = Column("id", Integer, nullable=False, primary_key=True, autoincrement=True)
  nome = Column("nome", String)
  email = Column("email", String, nullable=False)
  senha = Column("senha", String)
  ativo = Column("ativo", Boolean, default=True)
  admin = Column("admin", Boolean, default=False)
  
  #Inicializando a função usuario
  def __init__(self, nome, email, senha, ativo=True, admin=False):
    self.nome = nome
    self.email = email
    self.senha = senha
    self.ativo = ativo
    self.admin = admin

#Pedido
class Pedido(Base):
  __tablename__ = "pedido"
  
#Tabelas
  id = Column("id", Integer, primary_key=True, autoincrement=True)
  item = Column("item", Integer, ForeignKey("itens.id"))
  quantidade = Column("quantidade", Integer, default= 1)
  usuario = Column("usuario", ForeignKey("usuario.id"))
  valor = Column("valor", Float)
  status_pedido = Column("status_pedido", Enum(StatusPedido), default=StatusPedido.PENDENTE) #status: pendente, cancelado, finalizado
  
  #Inicializando a função pedido
  def __init__(self, usuario, item, quantidade, status_pedido=StatusPedido.PENDENTE, valor=0):
    self.usuario = usuario
    self.item = item
    self.quantidade = quantidade
    self.status_pedido = status_pedido
    self.valor = valor
  
  #def calcular_valor(self):
   # self.valor = sum(item.valor*item.quantidade for item in self.item)
    
#Itens
class Itens(Base):
  __tablename__="itens"
  
  #Tabela
  id = Column("id", Integer, primary_key=True, autoincrement=True)
  item = Column("item", String)
  qnt_estoque = Column("qnt_estoque", Integer)
  cor = Column("cor", String)
  valor_unitario = Column("valor_unitario", Float)
  desconto = Column("desconto", Float, default=0)
  
  #Inicializando a função item_pedido
  def __init__(self, item, qnt_estoque, cor, valor_unitario, desconto = 0):
    self.item = item
    self.qnt_estoque = qnt_estoque
    self.cor = cor
    self.valor_unitario = valor_unitario
    self.desconto = desconto
    
"""
#Criando migração de banco de dados com alembic

$1 Criando base de migração do banco de dados
python -m alembic init alembic #Criar pasta alembic

$2 Configurando conexão do banco de dados
em alembic.ini editar sqlalchemy.url -> sqlite://banco.db

$3 Configurando estrutura 
na pasta env.py importar a Base do seu documento.
  import sys
  import os
  sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
  
  from modelagem_db import Base
  target_metadata = Base.metadata
  
$4 - Criando banco de dados
Depois de configurado o passo $3, rodar no terminal: 
  python -m alembic revision --autogenerate -m "initial migration"
  
$5 Adicionando as tabelas
python -m alembic upgrade head

$6 Para novas alterações e atualização
  - criar versão de edição: python -m alembic revision --autogenerate -m "mensagem"
  - implementar: python -m alembic upgrade head
"""
