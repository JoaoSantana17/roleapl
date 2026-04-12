import os
import base64
import tempfile
import oracledb
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
WALLET_B64   = os.getenv("ORACLE_WALLET_B64")
WALLET_PASS  = os.getenv("ORACLE_WALLET_PASSWORD")

if not DATABASE_URL:
    raise RuntimeError("DATABASE_URL não definida.")
if not WALLET_B64:
    raise RuntimeError("ORACLE_WALLET_B64 não definida.")

wallet_dir  = tempfile.mkdtemp()
wallet_path = os.path.join(wallet_dir, "ewallet.pem")
with open(wallet_path, "wb") as f:
    f.write(base64.b64decode(WALLET_B64))

oracledb.defaults.wallet_location = wallet_dir
oracledb.defaults.wallet_password  = WALLET_PASS

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