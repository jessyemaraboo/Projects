#Rota de pedido

#Bibliotecas
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session #Abrir sessões
from funcionalidades.dependencias import pegar_sessao, verificar_token
from funcionalidades.schemas import PedidoSchema, ListarPedidosUsuario, ItemSchema
from banco_de_dados.modelagem_db import Pedido, Usuario, Itens
from typing import List
from funcionalidades.enums import StatusPedido
#Prefixo de rota
order_router = APIRouter(prefix="/pedidos", tags = ["pedido"], dependencies=[Depends(verificar_token)])

#Rota de pedido: método GET
@order_router.get("/")
async def pedido():
  return {"mensagem":f"Aqui você administra e vê seus pedidos"}

@order_router.get("/consultar-produtos", response_model=List[ItemSchema])
async def consultar_produtos(session: Session = Depends(pegar_sessao), usuario: Usuario = Depends(verificar_token)):

  itens = session.query(Itens).all()
  
  return itens

#Rota de pedido: método POST
@order_router.post("/fazer_pedido")
async def fazer_pedido(pedido_schema: PedidoSchema,
                       session: Session= Depends(pegar_sessao),
                       usuario: Usuario = Depends(verificar_token)):
  
    item = session.query(Itens).filter(Itens.id == pedido_schema.item).first()
    
    if not item:
      #404 Not found
      raise HTTPException(status_code= 404, detail="Item não encontado")
    
    elif item.qnt_estoque < pedido_schema.quantidade:
      raise HTTPException(status_code=400, detail="Estoque insuficiente.")
    
    elif item.desconto >=0:
      desconto = (item.valor_unitario*item.desconto)*pedido_schema.quantidade
    
    #Atualizar estoque
    item.qnt_estoque -= pedido_schema.quantidade
    pedido = Pedido(usuario = usuario.id, 
                    item = pedido_schema.item, 
                    quantidade = pedido_schema.quantidade,
                    valor=(item.valor_unitario*pedido_schema.quantidade)-desconto
                    )
    session.add(pedido)
    session.commit()
    session.refresh(pedido)
    return{
            "Id_de_pedido": f"{pedido.id}",
            "valor_total": f"R${pedido.valor}",
            "Desconto recebido": f"{item.desconto*100}%",
            "mensagem": f"Obrigada por nos escolher, {usuario.id}"
           
           }

@order_router.post("/{pedido_id}/cancelar")
async def cancelar_pedido(pedido_id: int, 
                          session: Session= Depends(pegar_sessao), 
                          usuario: Usuario = Depends(verificar_token)):
  
  pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()
  
  if not pedido:
    #404 Not found
    raise  HTTPException(status_code=404, detail="Pedido não encontrado")
  
  if not usuario.admin and usuario.id != pedido.usuario:
    #403 forbidden
    raise HTTPException(status_code=403, detail="Você não tem autorização para fazer essa modificação")
  
  if pedido.status_pedido == StatusPedido.CANCELADO:
    raise HTTPException(status_code=400,detail="Este pedido já foi cancelado")
  
  if pedido.status_pedido != StatusPedido.PENDENTE:
    raise HTTPException(status_code=400, detail="Somente pedidos pendentes podem ser cancelados. Em caso de pedidos finalizados, abra um chamado e avaliaremos o seu caso.")
  
  itens = session.query(Itens).filter(Itens.id == pedido.item).first()
  
  if not itens:
    raise HTTPException(status_code=404, detail="Item não encontrado")
  
  try:
    itens.qnt_estoque += pedido.quantidade
    pedido.status_pedido = StatusPedido.CANCELADO
    session.commit()#salva edições no banco de dados
  
  except Exception:
    session.rollback()#desfaz alterações atuais
    raise HTTPException(status_code=500, detail="Erro ao cancelar pedido, tente novamente")
  
  return{
    "mensagem": f"Seu pedido de id: {pedido.id}, foi cancelado com sucesso!",
    "pedido": pedido
  }

#Excluir pedido
@order_router.post("/{id_item_pedido}/remover-item")
async def remover_item_pedido(id_item_pedido: int, 
                              quantidade: int,
                              session: Session= Depends(pegar_sessao), 
                              usuario: Usuario = Depends(verificar_token)):
  
  #Verificar se o item do produto é igual ao item do produto pedido:
  item_pedido = session.query(Pedido).filter(Pedido.id == id_item_pedido).first()
  
  if not item_pedido:
    raise  HTTPException(status_code=404, detail="Item não consta em pedido")
    
  #Verificar quantidade solicitada
  if item_pedido.quantidade is None or quantidade > item_pedido.quantidade or quantidade < 1:
      raise HTTPException(status_code=400, detail="Quantidade inválida para este pedido")
  
  #Verificar permissão
  if not usuario.admin and usuario.id != item_pedido.usuario:
    #403 Forbidden
    raise HTTPException(status_code=403, detail="Você não tem autorização para fazer essa modificação")
  
  #Encontrar produto no estoque e devolver quantidades 
  item = session.query(Itens).filter(Itens.id == item_pedido.item).first()
  
  if item:
    item.qnt_estoque += quantidade
  
  if quantidade == item_pedido.quantidade:
    session.delete(item_pedido)
    valor_atualizado = 0.0
    mensagem = f"O pedido de id {item_pedido} foi atualizado e os itens {item_pedido.item} removido"
      
  else:
    valor_unitario = item_pedido.valor / item_pedido.quantidade
    item_pedido.quantidade -=quantidade
    item_pedido.valor = valor_unitario * item_pedido.quantidade
    valor_atualizado = item_pedido.valor
    mensagem = f"Seu item de id {id_item_pedido}, quantidade {quantidade}removida com sucesso"
      
  #Salvar alterações
  session.commit() #salva edições no banco de dados
  
  return{
      "mensagem": mensagem,
      "valor atualizado": f"R${valor_atualizado:.2f}",
      "quantidades de pedidos": f"você ainda tem {len(item_pedido.item)}"
  }

#Visualizar um pedido
@order_router.get("/{id_pedido}/visualizar")
async def visualizar_pedido(pedido_id:int,
                            session: Session = Depends(pegar_sessao),
                            usuario: Usuario = Depends(verificar_token)):
  pedido = session.query(Pedido).filter(Pedido.id == pedido_id).first()
  if not pedido:
    #404 Not found
    raise  HTTPException(status_code=404, detail="Pedido não encontrado")
  if not usuario.admin and usuario.id != pedido.usuario:
    #403 forbidden
    raise HTTPException(status_code=403, detail="Você não tem autorização para fazer essa modificação")
  return {
    "quantidade_itens": pedido.quantidade,
    "pedido": pedido
  }

#Visualizar todos os pedidos
@order_router.get("/visualizar")
async def visualizar_todos_pedidos(
                            session: Session = Depends(pegar_sessao),
                            usuario: Usuario = Depends(verificar_token)
                            ):
  pedidos = session.query(Pedido, Itens).join(Itens, Pedido.item == Itens.id).filter(Pedido.usuario==usuario.id).all()
  resultado = []
  
  for pedido, item in pedidos:
      dados = ListarPedidosUsuario(
          id= pedido.id,
          item= pedido.item,
          nome_item= item.item,
          quantidade= pedido.quantidade,
          valor= pedido.valor,
          status_pedido= pedido.status_pedido
      )
      resultado.append(dados)
  return resultado

  

  


