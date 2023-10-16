from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

database_url = "sqlite:///mydatabase.db"
engine = create_engine(database_url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)

if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)

    users = session.query(User).all()

    for record in users:
        print( record.username + ", " + record.email)
    