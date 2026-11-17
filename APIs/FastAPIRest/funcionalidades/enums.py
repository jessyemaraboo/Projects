#Regras de status de pedido
from enum import Enum

class StatusPedido(str, Enum):
  PENDENTE = "PENDENTE"
  CANCELADO = "CANCELADO"
  FINALIZADO = "FINALIZADO"