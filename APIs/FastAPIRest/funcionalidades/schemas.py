#Criando esquemas de padronização de dados

#Bibliotecas
from pydantic import BaseModel, ConfigDict
from typing import Optional

#Criando esquemas

#Usuario
class UsuarioSchema(BaseModel):
  nome: str
  email: str
  senha: str
  ativo: Optional[bool]
  admin: Optional[bool]

  class config:
    from_attributes = True

#Pedido

class PedidoSchema(BaseModel):
  item: int
  quantidade: int
  
  class config:
    from_attributes = True

#Login
class LoginSchema(BaseModel):
  email: str
  senha: str
  
  class config:
    from_attributes = True

#Item
class ItemSchema(BaseModel):
  id: int
  item: str
  cor: str
  valor_unitario: float
  desconto: float
  qnt_estoque: int
  
  class config:
    from_attributes = True

#Resposta
class ListarPedidosUsuario(BaseModel):
  id: int
  item: int
  nome_item: str
  quantidade: float
  valor: float
  status_pedido: str 
  

  class config:
      from_attributes = True

class AtualizarItem(BaseModel):
  item: Optional[str]=None
  qnt_estoque: Optional[int]=None
  cor: Optional[str]=None
  valor_unitario: Optional[float]=None
  desconto: Optional[float]=None
  
  model_config = ConfigDict(from_attributes=True)
  
  class config:
        from_attributes = True