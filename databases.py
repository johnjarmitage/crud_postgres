#!/usr/bin/python3

"""
python 3.7

script to create SQL database and deploy
John Armitage 14/11/2019
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Compte(Base):
    __tablename__ = 'Compte'
    Id = Column(Integer, primary_key=True)
    Nom = Column(String)
    Description = Column(String)

    def __repr__(self):
        return "<Compte(Id='{}', Nom='{}', Description={})>"\
                .format(self.Id, self.Nom, self.Description)


class Bucket(Base):
    __tablename__ = 'Bucket'
    Id = Column(Integer, primary_key=True)
    Nom = Column(String)
    Taille = Column(String)
    Type = Column(String)
    compteId = Column(Integer)

    def __repr__(self):
        return "<Bucket(Id='{}', Nom='{}', Taille='{}', Type='{}', compteId='{}'>"\
                .format(self.Id, self.Nom, self.Taille, self.Type, self.compteId)
