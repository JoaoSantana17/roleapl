import os
import base64
import tempfile
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
WALLET_B64 = os.getenv("ORACLE_WALLET_B64")

if not DATABASE_URL:
    raise RuntimeError("Variável DATABASE_URL não definida.")
if not WALLET_B64:
    raise RuntimeError("Variável ORACLE_WALLET_B64 não definida.")

wallet_dir = tempfile.mkdtemp()
wallet_path = os.path.join(wallet_dir, "ewallet.pem")
with open(wallet_path, "wb") as f:
    f.write(base64.b64decode(WALLET_B64))

engine = create_engine(
    DATABASE_URL,
    echo=False,
    pool_pre_ping=True,
    connect_args={
        "wallet_location": wallet_dir,
        "wallet_password": os.getenv("ORACLE_WALLET_PASSWORD"),
    }
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()