#!/usr/bin/python3

"""
python 3.7

script to create SQL database and deploy
John Armitage 14/11/2019
"""

from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)