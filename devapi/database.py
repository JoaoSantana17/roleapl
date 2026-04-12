import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Oracle Cloud connection string
# Formato: oracle+oracledb://usuario:senha@host:porta/?service_name=NOME_SERVICO
# Exemplo Oracle Autonomous Database (ATP):
#   oracle+oracledb://admin:MinhaSenh@123@adb.sa-saopaulo-1.oraclecloud.com:1521/?service_name=role_high
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "oracle+oracledb://system:senha123@localhost:1521/?service_name=XEPDB1"
)

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
