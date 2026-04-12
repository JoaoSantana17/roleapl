from pydantic import BaseModel, EmailStr
from typing import Optional, List
from datetime import date, datetime


# ─────────────────────────────────────────
#  USUARIO
# ─────────────────────────────────────────

class UsuarioCreate(BaseModel):
    nome: str
    data_nascimento: Optional[date] = None
    telefone: Optional[str] = None
    email: str
    senha: str
    foto_perfil: Optional[str] = None
    privacidade: Optional[str] = "público"

class UsuarioUpdate(BaseModel):
    nome: Optional[str] = None
    data_nascimento: Optional[date] = None
    telefone: Optional[str] = None
    foto_perfil: Optional[str] = None
    privacidade: Optional[str] = None

class UsuarioOut(BaseModel):
    id_usuario: int
    nome: str
    email: str
    telefone: Optional[str] = None
    foto_perfil: Optional[str] = None
    privacidade: Optional[str] = None

    class Config:
        from_attributes = True


# ─────────────────────────────────────────
#  ROLE (Evento/Rolê)
# ─────────────────────────────────────────

class RoleCreate(BaseModel):
    id_criador: int
    nome: str
    descricao: Optional[str] = None
    localizacao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    tipo: Optional[str] = None
    status: Optional[str] = "ativo"

class RoleUpdate(BaseModel):
    nome: Optional[str] = None
    descricao: Optional[str] = None
    localizacao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    tipo: Optional[str] = None
    status: Optional[str] = None

class RoleOut(BaseModel):
    id_role: int
    id_criador: int
    nome: str
    descricao: Optional[str] = None
    localizacao: Optional[str] = None
    data_inicio: Optional[date] = None
    data_fim: Optional[date] = None
    tipo: Optional[str] = None
    status: Optional[str] = None

    class Config:
        from_attributes = True


# ─────────────────────────────────────────
#  PARTICIPACAO
# ─────────────────────────────────────────

class ParticipacaoCreate(BaseModel):
    id_usuario: int
    id_role: int
    meio_transporte: Optional[str] = None
    status: Optional[str] = "em_deslocamento"
    eta: Optional[int] = None
    hora_entrada: Optional[datetime] = None

class ParticipacaoUpdate(BaseModel):
    meio_transporte: Optional[str] = None
    status: Optional[str] = None
    eta: Optional[int] = None
    hora_entrada: Optional[datetime] = None

class ParticipacaoOut(BaseModel):
    id_participacao: int
    id_usuario: int
    id_role: int
    meio_transporte: Optional[str] = None
    status: Optional[str] = None
    eta: Optional[int] = None
    hora_entrada: Optional[datetime] = None

    class Config:
        from_attributes = True


# ─────────────────────────────────────────
#  PUBLICACAO
# ─────────────────────────────────────────

class PublicacaoCreate(BaseModel):
    id_usuario: int
    id_role: int
    conteudo: Optional[str] = None
    imagem: Optional[str] = None

class PublicacaoUpdate(BaseModel):
    conteudo: Optional[str] = None
    imagem: Optional[str] = None

class PublicacaoOut(BaseModel):
    id_publicacao: int
    id_usuario: int
    id_role: int
    conteudo: Optional[str] = None
    imagem: Optional[str] = None
    data_postagem: Optional[datetime] = None

    class Config:
        from_attributes = True


# ─────────────────────────────────────────
#  COMENTARIO
# ─────────────────────────────────────────

class ComentarioCreate(BaseModel):
    id_publicacao: int
    id_usuario: int
    conteudo: str

class ComentarioUpdate(BaseModel):
    conteudo: str

class ComentarioOut(BaseModel):
    id_comentario: int
    id_publicacao: int
    id_usuario: int
    conteudo: str
    data_comentario: Optional[datetime] = None

    class Config:
        from_attributes = True


# ─────────────────────────────────────────
#  NOTIFICACAO
# ─────────────────────────────────────────

class NotificacaoCreate(BaseModel):
    id_usuario: int
    mensagem: Optional[str] = None
    tipo: Optional[str] = None

class NotificacaoOut(BaseModel):
    id_notificacao: int
    id_usuario: int
    mensagem: Optional[str] = None
    tipo: Optional[str] = None
    data_hora: Optional[datetime] = None

    class Config:
        from_attributes = True


# ─────────────────────────────────────────
#  LOCALIZACAO
# ─────────────────────────────────────────

class LocalizacaoCreate(BaseModel):
    id_usuario: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    precisao: Optional[float] = None

class LocalizacaoOut(BaseModel):
    id_localizacao: int
    id_usuario: int
    latitude: Optional[float] = None
    longitude: Optional[float] = None
    precisao: Optional[float] = None
    data_hora: Optional[datetime] = None

    class Config:
        from_attributes = True


# ─────────────────────────────────────────
#  AMIZADE
# ─────────────────────────────────────────

class AmizadeCreate(BaseModel):
    id_usuario_1: int
    id_usuario_2: int
    status: Optional[str] = "pendente"

class AmizadeUpdate(BaseModel):
    status: str  # pendente | aceito | bloqueado

class AmizadeOut(BaseModel):
    id_amizade: int
    id_usuario_1: int
    id_usuario_2: int
    status: str
    data_criacao: Optional[datetime] = None

    class Config:
        from_attributes = True


# ─────────────────────────────────────────
#  AUDITORIA (somente leitura)
# ─────────────────────────────────────────

class AuditoriaOut(BaseModel):
    id_auditoria: int
    operacao: Optional[str] = None
    usuario_bd: Optional[str] = None
    data_op: Optional[datetime] = None
    id_usuario: Optional[int] = None
    nome_old: Optional[str] = None
    nome_new: Optional[str] = None
    email_old: Optional[str] = None
    email_new: Optional[str] = None

    class Config:
        from_attributes = True
