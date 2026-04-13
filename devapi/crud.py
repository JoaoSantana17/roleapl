from sqlalchemy.orm import Session
from typing import Optional
import models, schemas


def create_usuario(db: Session, data: schemas.UsuarioCreate):
    obj = models.Usuario(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_usuario(db: Session, id_usuario: int):
    return db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()

def get_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Usuario).offset(skip).limit(limit).all()

def update_usuario(db: Session, id_usuario: int, data: schemas.UsuarioUpdate):
    obj = get_usuario(db, id_usuario)
    if not obj: return None
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit(); db.refresh(obj)
    return obj

def delete_usuario(db: Session, id_usuario: int):
    obj = get_usuario(db, id_usuario)
    if not obj: return False
    # Deleta dependências antes
    db.query(models.Amizade).filter(
        (models.Amizade.id_usuario_1 == id_usuario) | (models.Amizade.id_usuario_2 == id_usuario)
    ).delete(synchronize_session=False)
    db.query(models.Participacao).filter(models.Participacao.id_usuario == id_usuario).delete(synchronize_session=False)
    db.query(models.Notificacao).filter(models.Notificacao.id_usuario == id_usuario).delete(synchronize_session=False)
    db.query(models.Localizacao).filter(models.Localizacao.id_usuario == id_usuario).delete(synchronize_session=False)
    db.query(models.Comentario).filter(models.Comentario.id_usuario == id_usuario).delete(synchronize_session=False)
    db.query(models.Publicacao).filter(models.Publicacao.id_usuario == id_usuario).delete(synchronize_session=False)
    db.query(models.Role).filter(models.Role.id_criador == id_usuario).delete(synchronize_session=False)
    db.delete(obj)
    db.commit()
    return True

def create_role(db: Session, data: schemas.RoleCreate):
    obj = models.Role(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_role(db: Session, id_role: int):
    return db.query(models.Role).filter(models.Role.id_role == id_role).first()

def get_roles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Role).offset(skip).limit(limit).all()

def update_role(db: Session, id_role: int, data: schemas.RoleUpdate):
    obj = get_role(db, id_role)
    if not obj: return None
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit(); db.refresh(obj)
    return obj

def delete_role(db: Session, id_role: int):
    obj = get_role(db, id_role)
    if not obj: return False
    db.delete(obj); db.commit()
    return True


def create_participacao(db: Session, data: schemas.ParticipacaoCreate):
    obj = models.Participacao(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_participacao(db: Session, id_participacao: int):
    return db.query(models.Participacao).filter(models.Participacao.id_participacao == id_participacao).first()

def get_participacoes(db: Session, id_role: Optional[int] = None, id_usuario: Optional[int] = None):
    q = db.query(models.Participacao)
    if id_role:    q = q.filter(models.Participacao.id_role == id_role)
    if id_usuario: q = q.filter(models.Participacao.id_usuario == id_usuario)
    return q.all()

def update_participacao(db: Session, id_participacao: int, data: schemas.ParticipacaoUpdate):
    obj = get_participacao(db, id_participacao)
    if not obj: return None
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit(); db.refresh(obj)
    return obj

def delete_participacao(db: Session, id_participacao: int):
    obj = get_participacao(db, id_participacao)
    if not obj: return False
    db.delete(obj); db.commit()
    return True


def create_publicacao(db: Session, data: schemas.PublicacaoCreate):
    obj = models.Publicacao(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_publicacao(db: Session, id_publicacao: int):
    return db.query(models.Publicacao).filter(models.Publicacao.id_publicacao == id_publicacao).first()

def get_publicacoes(db: Session, id_role: Optional[int] = None):
    q = db.query(models.Publicacao)
    if id_role: q = q.filter(models.Publicacao.id_role == id_role)
    return q.all()

def update_publicacao(db: Session, id_publicacao: int, data: schemas.PublicacaoUpdate):
    obj = get_publicacao(db, id_publicacao)
    if not obj: return None
    for k, v in data.model_dump(exclude_unset=True).items():
        setattr(obj, k, v)
    db.commit(); db.refresh(obj)
    return obj

def delete_publicacao(db: Session, id_publicacao: int):
    obj = get_publicacao(db, id_publicacao)
    if not obj: return False
    db.delete(obj); db.commit()
    return True


def create_comentario(db: Session, data: schemas.ComentarioCreate):
    obj = models.Comentario(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_comentario(db: Session, id_comentario: int):
    return db.query(models.Comentario).filter(models.Comentario.id_comentario == id_comentario).first()

def get_comentarios(db: Session, id_publicacao: Optional[int] = None):
    q = db.query(models.Comentario)
    if id_publicacao: q = q.filter(models.Comentario.id_publicacao == id_publicacao)
    return q.all()

def update_comentario(db: Session, id_comentario: int, data: schemas.ComentarioUpdate):
    obj = get_comentario(db, id_comentario)
    if not obj: return None
    obj.conteudo = data.conteudo
    db.commit(); db.refresh(obj)
    return obj

def delete_comentario(db: Session, id_comentario: int):
    obj = get_comentario(db, id_comentario)
    if not obj: return False
    db.delete(obj); db.commit()
    return True


def create_notificacao(db: Session, data: schemas.NotificacaoCreate):
    obj = models.Notificacao(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_notificacoes(db: Session, id_usuario: int):
    return db.query(models.Notificacao).filter(models.Notificacao.id_usuario == id_usuario).all()

def delete_notificacao(db: Session, id_notificacao: int):
    obj = db.query(models.Notificacao).filter(models.Notificacao.id_notificacao == id_notificacao).first()
    if not obj: return False
    db.delete(obj); db.commit()
    return True


def create_localizacao(db: Session, data: schemas.LocalizacaoCreate):
    obj = models.Localizacao(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_localizacoes(db: Session, id_usuario: int):
    return db.query(models.Localizacao).filter(models.Localizacao.id_usuario == id_usuario).all()

def get_ultima_localizacao(db: Session, id_usuario: int):
    return (
        db.query(models.Localizacao)
        .filter(models.Localizacao.id_usuario == id_usuario)
        .order_by(models.Localizacao.data_hora.desc())
        .first()
    )


def create_amizade(db: Session, data: schemas.AmizadeCreate):
    obj = models.Amizade(**data.model_dump())
    db.add(obj); db.commit(); db.refresh(obj)
    return obj

def get_amizade(db: Session, id_amizade: int):
    return db.query(models.Amizade).filter(models.Amizade.id_amizade == id_amizade).first()

def get_amizades(db: Session, id_usuario: int):
    return db.query(models.Amizade).filter(
        (models.Amizade.id_usuario_1 == id_usuario) | (models.Amizade.id_usuario_2 == id_usuario)
    ).all()

def update_amizade(db: Session, id_amizade: int, data: schemas.AmizadeUpdate):
    obj = get_amizade(db, id_amizade)
    if not obj: return None
    obj.status = data.status
    db.commit(); db.refresh(obj)
    return obj

def delete_amizade(db: Session, id_amizade: int):
    obj = get_amizade(db, id_amizade)
    if not obj: return False
    db.delete(obj); db.commit()
    return True



def get_auditorias(db: Session, id_usuario: Optional[int] = None, skip: int = 0, limit: int = 100):
    q = db.query(models.AuditoriaUsuario)
    if id_usuario: q = q.filter(models.AuditoriaUsuario.id_usuario == id_usuario)
    return q.order_by(models.AuditoriaUsuario.data_op.desc()).offset(skip).limit(limit).all()
