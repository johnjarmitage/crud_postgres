#!/home/armitage/miniconda3/envs/crud_postgres/bin/python3

"""
python 3.7

script to create SQL database and deploy
John Armitage 14/11/2019
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker

# define database that I created using psql
DATABASE_URI = 'postgres+psycopg2://postgres:password@localhost:5432/gekko_tp2'
engine = create_engine(DATABASE_URI)
Base = declarative_base()


# table Compte classe
class Compte(Base):
    __tablename__ = 'Compte'
    Id = Column(Integer, primary_key=True)
    Nom = Column(String)
    Description = Column(String)

    def __repr__(self):
        return "<Compte(Id='{}', Nom='{}', Description={})>"\
                .format(self.Id, self.Nom, self.Description)


# table Bucket classe
class Bucket(Base):
    __tablename__ = 'Bucket'
    Id = Column(Integer, primary_key=True)
    Nom = Column(String)
    Taille = Column(String)
    Type = Column(String)
    compteId = Column(Integer, ForeignKey("Compte.Id"))

    def __repr__(self):
        return "<Bucket(Id='{}', Nom='{}', Taille='{}', Type='{}', compteId='{}'>"\
                .format(self.Id, self.Nom, self.Taille, self.Type, self.compteId)


# create the tables
Base.metadata.create_all(engine)

# start a session to do some CRUD
Session = sessionmaker(bind=engine)
s = Session()

someone = Compte(
    Id=1,
    Nom='Ian Goodfellow',
    Description='775'
)

s.add(someone)
s.commit()
s.close()
