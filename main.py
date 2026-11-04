from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from itertools import count

app = FastAPI()

class TarefaEntrada(BaseModel):
    titulo: str
    concluida: bool = False


tarefas = []
gerador_ids = count(1) 

# @app.post('/tarefas', status_code=201)
# def criar_tarefa(tarefa: TarefaEntrada):
#    return{
#       "Mensagem": "Tarefa Recebida com sucesso",
#       "tarefa": tarefa.model_dump()
#    }

# @app.post("/tarefas", status_code=201)
# def criar_tarefa(tarefa: TarefaEntrada):
#     nova_tarefa = {
#        "id": len(tarefas) + 1,
#        "titulo": tarefa.titulo,
#        "concluida": tarefa.concluida
#     }

#     tarefas.append(nova_tarefa)
#     return nova_tarefa

# @app.get("/tarefas")
# def listar_tarefas():
#     return tarefas

@app.post("/tarefas",  status_code=201)
def criar_tarefa(tarefa: TarefaEntrada):
    nova_tarefa = {
      "id": next(gerador_ids),
      "titulo" : tarefa.titulo,
      "concluida": tarefa.concluida

   }
    tarefas.append(nova_tarefa)

    return nova_tarefa

@app.get("/tarefas")
def listar_tarefas():
    return tarefas

# @app.get("/tarefas/{tarefa_id}")
# def buscar_tarefa(tarefa_id : int):
#     for tarefa in tarefas:
#       if tarefa["id"] == tarefa_id:
#          return tarefa

#     raise HTTPException(
#        status_code= 404,
#        detail="Tarefa não encontrada"
#     )




@app.get("/tarefas/{tarefa_id}")
def buscar_tarefa(tarefa_id: int):
    for tarefa in tarefas:
       if tarefa["id"] == tarefa_id:
          return tarefa


    raise HTTPException(
       status_code=404,
       detail="tarefa não encontrada"                 
       )





@app.get("/")
def inicio():
  return {"mensagem" :"Wellow World api is runnig"}

@app.get("/tarefas/{tarefa_id}")
def buscar_tarefa(tarefa_id: int):
  return{
    "id": tarefa_id,
    "titulo": "estudar api",
    "concluida": False
  }



@app.get("/nome/estudantes/{nome}")
def nome_feio(nome : str):
  return {
    "id": 4,
    "Nome": "É um boboca" if nome == "Murilo" else "Não é boboca",
    "Test": 32
  }


# @app.put("/tarefas/{tarefa_id}")
# def atualizar_tarefa(tarefa_id: int, dados: TarefaEntrada):
#     for tarefa in tarefas:
#       if tarefa["id"] == tarefa_id:
#           tarefa["titulo"] = dados.titulo
#           tarefa["concluida"] = dados.concluida

#           return tarefa


#     raise HTTPException(
#        status_code=404,
#        detail="tarefa não encontrada"
#     )


@app.put("/tarefas/{tarefa_id}")
def atualizar_tarefa(tarefa_id : int, dados : TarefaEntrada ):
    for tarefa in tarefas:
        if tarefa["id"] == tarefa_id:
           tarefa["titulo"] = dados.titulo
           tarefa["concluida"] == dados.concluida

           return tarefa

    raise HTTPException(
       status_code=404,
       detail="Tarefa não encontrada"
    )

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    for tarefa in tarefas:
      if tarefa["id"] == tarefa_id:
          tarefas.remove(tarefa)
          
          return{
             "mensagem": "tarefa excluida com sucesso",
             "id": tarefa_id

          }

    raise HTTPException(
       status_code=404,
       detail="Não encontrada"
    )

