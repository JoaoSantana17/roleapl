from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas, crud
from database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Rolé API",
    description="API REST do app Rolé — Oracle Database Cloud",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/usuarios/", response_model=schemas.UsuarioOut, tags=["Usuários"])
def criar_usuario(data: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    return crud.create_usuario(db, data)

@app.get("/usuarios/", response_model=List[schemas.UsuarioOut], tags=["Usuários"])
def listar_usuarios(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_usuarios(db, skip, limit)

@app.get("/usuarios/{id_usuario}", response_model=schemas.UsuarioOut, tags=["Usuários"])
def buscar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    obj = crud.get_usuario(db, id_usuario)
    if not obj: raise HTTPException(404, "Usuário não encontrado")
    return obj

@app.put("/usuarios/{id_usuario}", response_model=schemas.UsuarioOut, tags=["Usuários"])
def atualizar_usuario(id_usuario: int, data: schemas.UsuarioUpdate, db: Session = Depends(get_db)):
    obj = crud.update_usuario(db, id_usuario, data)
    if not obj: raise HTTPException(404, "Usuário não encontrado")
    return obj

@app.delete("/usuarios/{id_usuario}", tags=["Usuários"])
def deletar_usuario(id_usuario: int, db: Session = Depends(get_db)):
    if not crud.delete_usuario(db, id_usuario):
        raise HTTPException(404, "Usuário não encontrado")
    return {"mensagem": "Usuário deletado com sucesso"}



@app.post("/roles/", response_model=schemas.RoleOut, tags=["Roles"])
def criar_role(data: schemas.RoleCreate, db: Session = Depends(get_db)):
    if not crud.get_usuario(db, data.id_criador):
        raise HTTPException(404, "Criador não encontrado")
    return crud.create_role(db, data)

@app.get("/roles/", response_model=List[schemas.RoleOut], tags=["Roles"])
def listar_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_roles(db, skip, limit)

@app.get("/roles/{id_role}", response_model=schemas.RoleOut, tags=["Roles"])
def buscar_role(id_role: int, db: Session = Depends(get_db)):
    obj = crud.get_role(db, id_role)
    if not obj: raise HTTPException(404, "Rolê não encontrado")
    return obj

@app.put("/roles/{id_role}", response_model=schemas.RoleOut, tags=["Roles"])
def atualizar_role(id_role: int, data: schemas.RoleUpdate, db: Session = Depends(get_db)):
    obj = crud.update_role(db, id_role, data)
    if not obj: raise HTTPException(404, "Rolê não encontrado")
    return obj

@app.delete("/roles/{id_role}", tags=["Roles"])
def deletar_role(id_role: int, db: Session = Depends(get_db)):
    if not crud.delete_role(db, id_role):
        raise HTTPException(404, "Rolê não encontrado")
    return {"mensagem": "Rolê deletado com sucesso"}


@app.post("/participacoes/", response_model=schemas.ParticipacaoOut, tags=["Participações"])
def criar_participacao(data: schemas.ParticipacaoCreate, db: Session = Depends(get_db)):
    if not crud.get_usuario(db, data.id_usuario):
        raise HTTPException(404, "Usuário não encontrado")
    if not crud.get_role(db, data.id_role):
        raise HTTPException(404, "Rolê não encontrado")
    return crud.create_participacao(db, data)

@app.get("/participacoes/", response_model=List[schemas.ParticipacaoOut], tags=["Participações"])
def listar_participacoes(id_role: Optional[int] = None, id_usuario: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_participacoes(db, id_role, id_usuario)

@app.get("/participacoes/{id_participacao}", response_model=schemas.ParticipacaoOut, tags=["Participações"])
def buscar_participacao(id_participacao: int, db: Session = Depends(get_db)):
    obj = crud.get_participacao(db, id_participacao)
    if not obj: raise HTTPException(404, "Participação não encontrada")
    return obj

@app.put("/participacoes/{id_participacao}", response_model=schemas.ParticipacaoOut, tags=["Participações"])
def atualizar_participacao(id_participacao: int, data: schemas.ParticipacaoUpdate, db: Session = Depends(get_db)):
    obj = crud.update_participacao(db, id_participacao, data)
    if not obj: raise HTTPException(404, "Participação não encontrada")
    return obj

@app.delete("/participacoes/{id_participacao}", tags=["Participações"])
def deletar_participacao(id_participacao: int, db: Session = Depends(get_db)):
    if not crud.delete_participacao(db, id_participacao):
        raise HTTPException(404, "Participação não encontrada")
    return {"mensagem": "Participação removida"}



@app.post("/publicacoes/", response_model=schemas.PublicacaoOut, tags=["Publicações"])
def criar_publicacao(data: schemas.PublicacaoCreate, db: Session = Depends(get_db)):
    if not crud.get_usuario(db, data.id_usuario): raise HTTPException(404, "Usuário não encontrado")
    if not crud.get_role(db, data.id_role): raise HTTPException(404, "Rolê não encontrado")
    return crud.create_publicacao(db, data)

@app.get("/publicacoes/", response_model=List[schemas.PublicacaoOut], tags=["Publicações"])
def listar_publicacoes(id_role: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_publicacoes(db, id_role)

@app.get("/publicacoes/{id_publicacao}", response_model=schemas.PublicacaoOut, tags=["Publicações"])
def buscar_publicacao(id_publicacao: int, db: Session = Depends(get_db)):
    obj = crud.get_publicacao(db, id_publicacao)
    if not obj: raise HTTPException(404, "Publicação não encontrada")
    return obj

@app.put("/publicacoes/{id_publicacao}", response_model=schemas.PublicacaoOut, tags=["Publicações"])
def atualizar_publicacao(id_publicacao: int, data: schemas.PublicacaoUpdate, db: Session = Depends(get_db)):
    obj = crud.update_publicacao(db, id_publicacao, data)
    if not obj: raise HTTPException(404, "Publicação não encontrada")
    return obj

@app.delete("/publicacoes/{id_publicacao}", tags=["Publicações"])
def deletar_publicacao(id_publicacao: int, db: Session = Depends(get_db)):
    if not crud.delete_publicacao(db, id_publicacao):
        raise HTTPException(404, "Publicação não encontrada")
    return {"mensagem": "Publicação deletada"}


@app.post("/comentarios/", response_model=schemas.ComentarioOut, tags=["Comentários"])
def criar_comentario(data: schemas.ComentarioCreate, db: Session = Depends(get_db)):
    if not crud.get_publicacao(db, data.id_publicacao): raise HTTPException(404, "Publicação não encontrada")
    if not crud.get_usuario(db, data.id_usuario): raise HTTPException(404, "Usuário não encontrado")
    return crud.create_comentario(db, data)

@app.get("/comentarios/", response_model=List[schemas.ComentarioOut], tags=["Comentários"])
def listar_comentarios(id_publicacao: Optional[int] = None, db: Session = Depends(get_db)):
    return crud.get_comentarios(db, id_publicacao)

@app.get("/comentarios/{id_comentario}", response_model=schemas.ComentarioOut, tags=["Comentários"])
def buscar_comentario(id_comentario: int, db: Session = Depends(get_db)):
    obj = crud.get_comentario(db, id_comentario)
    if not obj: raise HTTPException(404, "Comentário não encontrado")
    return obj

@app.put("/comentarios/{id_comentario}", response_model=schemas.ComentarioOut, tags=["Comentários"])
def atualizar_comentario(id_comentario: int, data: schemas.ComentarioUpdate, db: Session = Depends(get_db)):
    obj = crud.update_comentario(db, id_comentario, data)
    if not obj: raise HTTPException(404, "Comentário não encontrado")
    return obj

@app.delete("/comentarios/{id_comentario}", tags=["Comentários"])
def deletar_comentario(id_comentario: int, db: Session = Depends(get_db)):
    if not crud.delete_comentario(db, id_comentario):
        raise HTTPException(404, "Comentário não encontrado")
    return {"mensagem": "Comentário deletado"}


@app.post("/notificacoes/", response_model=schemas.NotificacaoOut, tags=["Notificações"])
def criar_notificacao(data: schemas.NotificacaoCreate, db: Session = Depends(get_db)):
    if not crud.get_usuario(db, data.id_usuario): raise HTTPException(404, "Usuário não encontrado")
    return crud.create_notificacao(db, data)

@app.get("/notificacoes/{id_usuario}", response_model=List[schemas.NotificacaoOut], tags=["Notificações"])
def listar_notificacoes(id_usuario: int, db: Session = Depends(get_db)):
    return crud.get_notificacoes(db, id_usuario)

@app.delete("/notificacoes/{id_notificacao}", tags=["Notificações"])
def deletar_notificacao(id_notificacao: int, db: Session = Depends(get_db)):
    if not crud.delete_notificacao(db, id_notificacao):
        raise HTTPException(404, "Notificação não encontrada")
    return {"mensagem": "Notificação removida"}


@app.post("/localizacoes/", response_model=schemas.LocalizacaoOut, tags=["Localização"])
def registrar_localizacao(data: schemas.LocalizacaoCreate, db: Session = Depends(get_db)):
    if not crud.get_usuario(db, data.id_usuario): raise HTTPException(404, "Usuário não encontrado")
    return crud.create_localizacao(db, data)

@app.get("/localizacoes/{id_usuario}/ultima", response_model=schemas.LocalizacaoOut, tags=["Localização"])
def ultima_localizacao(id_usuario: int, db: Session = Depends(get_db)):
    obj = crud.get_ultima_localizacao(db, id_usuario)
    if not obj: raise HTTPException(404, "Nenhuma localização encontrada")
    return obj

@app.get("/localizacoes/{id_usuario}", response_model=List[schemas.LocalizacaoOut], tags=["Localização"])
def historico_localizacao(id_usuario: int, db: Session = Depends(get_db)):
    return crud.get_localizacoes(db, id_usuario)



@app.post("/amizades/", response_model=schemas.AmizadeOut, tags=["Amizades"])
def criar_amizade(data: schemas.AmizadeCreate, db: Session = Depends(get_db)):
    return crud.create_amizade(db, data)

@app.get("/amizades/{id_usuario}", response_model=List[schemas.AmizadeOut], tags=["Amizades"])
def listar_amizades(id_usuario: int, db: Session = Depends(get_db)):
    return crud.get_amizades(db, id_usuario)

@app.put("/amizades/{id_amizade}", response_model=schemas.AmizadeOut, tags=["Amizades"])
def atualizar_amizade(id_amizade: int, data: schemas.AmizadeUpdate, db: Session = Depends(get_db)):
    obj = crud.update_amizade(db, id_amizade, data)
    if not obj: raise HTTPException(404, "Amizade não encontrada")
    return obj

@app.delete("/amizades/{id_amizade}", tags=["Amizades"])
def deletar_amizade(id_amizade: int, db: Session = Depends(get_db)):
    if not crud.delete_amizade(db, id_amizade):
        raise HTTPException(404, "Amizade não encontrada")
    return {"mensagem": "Amizade removida"}



@app.get("/auditoria/", response_model=List[schemas.AuditoriaOut], tags=["Auditoria"])
def listar_auditoria(id_usuario: Optional[int] = None, skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_auditorias(db, id_usuario, skip, limit)


@app.get("/", tags=["Root"])
def root():
    return {"mensagem": "Rolé API v2 — Oracle Database Cloud", "docs": "/docs"}
