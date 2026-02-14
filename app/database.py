from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

DATABASE_URL=os.getenv("DATABASE_URL")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL is not set in environment variables")
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL=DATABASE_URL.replace("postgres://",'postgresql://',1)

print("DATABASE_URL Being Used:",DATABASE_URL);
engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base = declarative_base()