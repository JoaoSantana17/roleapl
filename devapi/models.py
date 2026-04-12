from sqlalchemy import (
    Column, Integer, String, Date, Float, DateTime,
    Text, Numeric, ForeignKey, CheckConstraint
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Usuario(Base):
    __tablename__ = "usuario"

    id_usuario      = Column(Integer, primary_key=True, index=True)
    nome            = Column(String(100), nullable=False)
    data_nascimento = Column(Date)
    telefone        = Column(String(20))
    email           = Column(String(100), unique=True, nullable=False)
    senha           = Column(String(255), nullable=False)
    foto_perfil     = Column(String(255))
    privacidade     = Column(String(20))

    __table_args__ = (
        CheckConstraint("privacidade IN ('público','amigos','privado')", name="ck_usuario_privacidade"),
    )

    roles_criados  = relationship("Role", back_populates="criador", foreign_keys="Role.id_criador")
    participacoes  = relationship("Participacao", back_populates="usuario")
    publicacoes    = relationship("Publicacao", back_populates="usuario")
    comentarios    = relationship("Comentario", back_populates="usuario")
    notificacoes   = relationship("Notificacao", back_populates="usuario")
    localizacoes   = relationship("Localizacao", back_populates="usuario")
    amizades_1     = relationship("Amizade", back_populates="usuario1", foreign_keys="Amizade.id_usuario_1")
    amizades_2     = relationship("Amizade", back_populates="usuario2", foreign_keys="Amizade.id_usuario_2")


class Role(Base):
    __tablename__ = "role"

    id_role      = Column(Integer, primary_key=True, index=True)
    id_criador   = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    nome         = Column(String(100), nullable=False)
    descricao    = Column(Text)
    localizacao  = Column(String(255))
    data_inicio  = Column(Date)
    data_fim     = Column(Date)
    tipo         = Column(String(30))
    status       = Column(String(20), default="ativo")

    __table_args__ = (
        CheckConstraint("tipo IN ('churrasco','bar','show','reunião','outro')", name="ck_role_tipo"),
        CheckConstraint("status IN ('ativo','finalizado')", name="ck_role_status"),
    )

    criador       = relationship("Usuario", back_populates="roles_criados", foreign_keys=[id_criador])
    participacoes = relationship("Participacao", back_populates="role")
    publicacoes   = relationship("Publicacao", back_populates="role")


class Participacao(Base):
    __tablename__ = "participacao"

    id_participacao = Column(Integer, primary_key=True, index=True)
    id_usuario      = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_role         = Column(Integer, ForeignKey("role.id_role"), nullable=False)
    meio_transporte = Column(String(30))
    status          = Column(String(30))
    eta             = Column(Integer)
    hora_entrada    = Column(DateTime)

    __table_args__ = (
        CheckConstraint("meio_transporte IN ('carro','uber','metrô','ônibus','a pé')", name="ck_part_transporte"),
        CheckConstraint("status IN ('em_deslocamento','presente','ausente','finalizado')", name="ck_part_status"),
    )

    usuario = relationship("Usuario", back_populates="participacoes")
    role    = relationship("Role", back_populates="participacoes")


class Publicacao(Base):
    __tablename__ = "publicacao"

    id_publicacao = Column(Integer, primary_key=True, index=True)
    id_usuario    = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_role       = Column(Integer, ForeignKey("role.id_role"), nullable=False)
    conteudo      = Column(Text)
    imagem        = Column(String(255))
    data_postagem = Column(DateTime, server_default=func.current_timestamp())

    usuario    = relationship("Usuario", back_populates="publicacoes")
    role       = relationship("Role", back_populates="publicacoes")
    comentarios = relationship("Comentario", back_populates="publicacao")


class Comentario(Base):
    __tablename__ = "comentario"

    id_comentario   = Column(Integer, primary_key=True, index=True)
    id_publicacao   = Column(Integer, ForeignKey("publicacao.id_publicacao"), nullable=False)
    id_usuario      = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    conteudo        = Column(Text, nullable=False)
    data_comentario = Column(DateTime, server_default=func.current_timestamp())

    publicacao = relationship("Publicacao", back_populates="comentarios")
    usuario    = relationship("Usuario", back_populates="comentarios")


class Notificacao(Base):
    __tablename__ = "notificacao"

    id_notificacao = Column(Integer, primary_key=True, index=True)
    id_usuario     = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    mensagem       = Column(String(255))
    tipo           = Column(String(50))
    data_hora      = Column(DateTime, server_default=func.current_timestamp())

    __table_args__ = (
        CheckConstraint("tipo IN ('saiu','chegou','rolê finalizado')", name="ck_notif_tipo"),
    )

    usuario = relationship("Usuario", back_populates="notificacoes")


class Localizacao(Base):
    __tablename__ = "localizacao"

    id_localizacao = Column(Integer, primary_key=True, index=True)
    id_usuario     = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    latitude       = Column(Numeric(10, 7))
    longitude      = Column(Numeric(10, 7))
    precisao       = Column(Float)
    data_hora      = Column(DateTime, server_default=func.current_timestamp())

    usuario = relationship("Usuario", back_populates="localizacoes")


class Amizade(Base):
    __tablename__ = "amizade"

    id_amizade   = Column(Integer, primary_key=True, index=True)
    id_usuario_1 = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    id_usuario_2 = Column(Integer, ForeignKey("usuario.id_usuario"), nullable=False)
    status       = Column(String(30), default="pendente")
    data_criacao = Column(DateTime, server_default=func.current_timestamp())

    __table_args__ = (
        CheckConstraint("status IN ('pendente','aceito','bloqueado')", name="ck_amizade_status"),
    )

    usuario1 = relationship("Usuario", back_populates="amizades_1", foreign_keys=[id_usuario_1])
    usuario2 = relationship("Usuario", back_populates="amizades_2", foreign_keys=[id_usuario_2])


class AuditoriaUsuario(Base):
    __tablename__ = "auditoria_usuario"

    id_auditoria = Column(Integer, primary_key=True, index=True)
    operacao     = Column(String(10))
    usuario_bd   = Column(String(50))
    data_op      = Column(DateTime, server_default=func.current_timestamp())
    id_usuario   = Column(Integer)
    nome_old     = Column(String(100))
    nome_new     = Column(String(100))
    email_old    = Column(String(100))
    email_new    = Column(String(100))
