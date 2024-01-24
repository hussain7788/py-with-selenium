from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

engine = create_engine('sqlite:///test.db')

Base = declarative_base()

SessionLocal = sessionmaker(bind=engine, autoflush=False,
                            expire_on_commit=False, autocommit=False)
