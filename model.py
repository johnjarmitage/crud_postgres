#!/home/armitage/miniconda3/envs/crud_postgres/bin/python3

"""
python 3.7

script to create SQL database and deploy
John Armitage 14/11/2019
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, CHAR, ForeignKey

Base = declarative_base()


# table Compte classe
class Compte(Base):
    __tablename__ = 'Compte'
    Id = Column(Integer, primary_key=True)
    Nom = Column(CHAR(75))
    Description = Column(CHAR(150))

    def __repr__(self):
        return "<Compte(Id='{}', Nom='{}', Description={})>"\
                .format(self.Id, self.Nom, self.Description)


# table Bucket classe
class Bucket(Base):
    __tablename__ = 'Bucket'
    Id = Column(Integer, primary_key=True)
    Nom = Column(CHAR(75))
    Taille = Column(CHAR(15))
    Type = Column(CHAR(50))
    compteId = Column(Integer, ForeignKey("Compte.Id"))

    def __repr__(self):
        return "<Bucket(Id='{}', Nom='{}', Taille='{}', Type='{}', compteId='{}'>"\
                .format(self.Id, self.Nom, self.Taille, self.Type, self.compteId)