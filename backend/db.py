import sqlalchemy
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.schema import Column
from sqlalchemy.types import String

DATABASE_URL = "postgresql://user:pass@postgres:5432/test_db"

engine = sqlalchemy.create_engine(DATABASE_URL, echo=True)
base = declarative_base()


class Sample(base):
    __tablename__ = "sample"
    date: str = Column(String, primary_key=True)


base.metadata.create_all(engine)

SessionMaker = sessionmaker(engine)
