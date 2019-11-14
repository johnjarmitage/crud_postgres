#!/usr/bin/python3

"""
python 3.7

script to create SQL database and deploy
John Armitage 14/11/2019
"""

# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"

DATABASE_URI = 'postgres+psycopg2://postgres:password@localhost:5432/gekko_tp1'