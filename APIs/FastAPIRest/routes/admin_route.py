#Rota de administradores

#Bibliotecas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session #Abrir sessões
from funcionalidades.dependencias import pegar_sessao, verificar_token
from funcionalidades.schemas import ItemSchema, AtualizarItem
from banco_de_dados.modelagem_db import Pedido, Usuario, Itens
from funcionalidades.enums import StatusPedido

admin_router = APIRouter(prefix="/admin", tags = ["admin"], dependencies=[Depends(verificar_token)])

@admin_router.get("/")
async def admin():
  return {"mensagem":f"Área do administrador."}

#Operações do Admin
@admin_router.get("pedidos/listar_pedidos")
async def listar_pedidos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):
  
  if not usuario.admin:
    raise HTTPException(status_code=401, detail="Você não tem autorização para fazer essa autorização")
  else:
    pedidos = session.query(Pedido).all()
    return {
      "pedidos": pedidos
    }

@admin_router.post("/itens/adicionar-item")
async def adicionar_item(item_schema: ItemSchema, 
                         session: Session = Depends(pegar_sessao), 
                         usuario: Usuario= Depends(verificar_token)):
  if not usuario.admin:
    raise HTTPException(status_code=401, detail="Você não tem autorização para realizar esta operação.")
  
  novo_item = Itens(item_schema.item, item_schema.qnt_estoque, item_schema.cor, item_schema.valor_unitario, item_schema.desconto)
  
  session.add(novo_item)
  session.commit()
  return{"mensagem": "Item adicionado com sucesso",
         "item-id": novo_item.id,
         "valor_pedido": novo_item.valor_unitario,
         "Desconto": f"Para este item o desconto é de {novo_item.desconto*100}%"
         }

@admin_router.patch("/itens/{item_id}/atualizar-item")
async def atualizar_item(item_id: int,
                         dados: AtualizarItem,
                         session: Session = Depends(pegar_sessao),
                         usuario: Usuario =  Depends(verificar_token)):

  if not usuario.admin:
      raise HTTPException(status_code=403, detail="Você não tem autorização para realizar esta operação")
    
  item = session.query(Itens).filter(Itens.id == item_id).first()
    
  if not item:
      raise HTTPException(status_code=404, detail="Item não encontrado")
    
  atualizar = dados.model_dump(exclude_unset=True)
  
  for campo, valor in atualizar.items():
    if campo == "qnt_estoque":
      item.qnt_estoque += valor
    else: 
      setattr(item, campo, valor)
  
  session.commit()
  session.refresh(item)
  
  return {
        "mensagem":"Item atualizado com sucesso."
        }
  
#Aprovar e finalizar pedido  
@admin_router.put("/pedidos/{pedido_id}/finalizar")
async def finalizar_pedido(pedido_id: int, 
                          session: Session= Depends(pegar_sessao), 
                          usuario: Usuario = Depends(verificar_token)):
  
  pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()
  
  if not pedido:
    #404 Not found
    raise  HTTPException(status_code=404, detail="Pedido não encontrado")
  
  if not usuario.admin:
    #403 Forbidden
    raise HTTPException(status_code=403, detail="Você não tem autorização para fazer essa modificação")
  
  if pedido.status_pedido == StatusPedido.CANCELADO:
    raise HTTPException(status_code=400, detail="Não é possível finalizar um pedido cancelado")
  
  if pedido.status_pedido == StatusPedido.FINALIZADO:
    raise HTTPException(status_code=400, detail="Este pedido já está finalizado")
  
  pedido.status_pedido = StatusPedido.FINALIZADO
  session.commit() #salva edições no banco de dados
  return{
    "mensagem": f"Seu pedido de id: {pedido.id}, foi finalizado com sucesso!",
    "pedido": pedido
  }
  

      
  
  
  