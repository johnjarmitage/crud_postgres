#!/home/armitage/miniconda3/envs/crud_postgres/bin/python3

"""
python 3.7

script to create SQL database and deploy
John Armitage 14/11/2019

Usage:
    crud.py table options
"""

import warnings
import argparse
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

try:
    from model import Base, Compte, Bucket
except ImportError:
    warnings.warn('Need to define the tables, see model.py', ImportWarning)
try:
    from config import DATABASE_URI
except ImportError:
    warnings.warn('Need to define the database, see config.py', ImportWarning)


# CREATE
def create(session, thing):
    session.add(thing)
    s.commit()


# SELECT and optionally DELETE
def find_by_id(session, table, numb, opt):
    query = session.query(table).filter_by(Id=numb)
    if opt == 'del':
        session.delete(query.one())
        return 'selection deleted'
    else:
        return query.all()


def find_by_name(session, table, word, opt):
    query = session.query(table).filter_by(Nom=word)
    if opt == 'del':
        session.delete(query.one())
        return 'selection deleted'
    else:
        return query.all()


def find_by_description(session, table, words, opt):
    query = session.query(table).filter_by(Description=words)
    if opt == 'del':
        session.delete(query.one())
        return 'selection deleted'
    else:
        return query.all()


def find_by_taille(session, table, word, opt):
    query = session.query(table).filter_by(Taille=word)
    if opt == 'del':
        session.delete(query.one())
        return 'selection deleted'
    else:
        return query.all()


def find_by_type(session, table, word, opt):
    query = session.query(table).filter_by(Type=word)
    if opt == 'del':
        session.delete(query.one())
        return 'selection deleted'
    else:
        return query.all()


#MODIFY
def modify_name_by_id(session, table, id, word):
    query = session.query(table).filter_by(Id=id).one()
    query.Nom = word
    session.add(query)


def modify_description_by_id(session, table, id, word):
    query = session.query(table).filter_by(Id=id).one()
    query.Description = word
    session.add(query)


def modify_taille_by_id(session, table, id, word):
    query = session.query(table).filter_by(Id=id).one()
    query.Taille = word
    session.add(query)


def modify_type_by_id(session, table, id, word):
    query = session.query(table).filter_by(Id=id).one()
    query.Type = word
    session.add(query)


if __name__ == '__main__':
    engine = create_engine(DATABASE_URI)
    Base.metadata.create_all(engine)

    parser = argparse.ArgumentParser(description='query a SQL database')
    parser.add_argument('table', help='table in database')
    parser.add_argument('-c', '--create', nargs='*', help='create a row')
    parser.add_argument('-q', '--query', nargs='*', help='find: -q [type] [query], eg: -q Id 1')
    parser.add_argument('-m', '--modify', nargs='*', help='modify: -m [id] [column] [new], eg: -m 1 Nom John')
    parser.add_argument('-d', '--delete', nargs='*', help='delete: -d [type] [query], eg: -q Id 1')

    args = parser.parse_args()

    # start a session to do some CRUD
    Session = sessionmaker(bind=engine)
    s = Session()

    if args.table == 'Compte':
        dbtable = Compte
    elif args.table == 'Bucket':
        dbtable = Bucket
    else:
        print('table does not exist')
        dbtable = ' '

    if args.create:
        if args.table == 'Compte':
            someone = Compte(
                Id=int(args.create[0]),
                Nom=args.create[1],
                Description=args.create[2]
            )
            create(s, someone)
        if args.table == 'Bucket':
            someone = Bucket(
                Id=int(args.create[0]),
                Nom=args.create[1],
                Taille=args.create[2],
                Type=args.create[3],
                compteId=int(args.create[4])
            )
            create(s, someone)

    if args.query:
        if args.query[0] == 'Id':
            print(find_by_id(s, dbtable, int(args.query[1]), ' '))
        elif args.query[0] == 'Nom':
            print(find_by_name(s, dbtable, args.query[1], ' '))
        elif args.query[0] == 'Description':
            print(find_by_description(s, dbtable, args.query[1], ' '))
        elif args.query[0] == 'Taille':
            print(find_by_taille(s, dbtable, args.query[1], ' '))
        elif args.query[0] == 'Type':
            print(find_by_type(s, dbtable, args.query[1], ' '))
        else:
            print('invalid search: ' + args.query[1])

    if args.delete:
        if args.delete[0] == 'Id':
            print(find_by_id(s, dbtable, int(args.delete[1]), 'del'))
        elif args.delete[0] == 'Nom':
            print(find_by_name(s, dbtable, args.delete[1], 'del'))
        elif args.delete[0] == 'Description':
            print(find_by_description(s, dbtable, args.delete[1], 'del'))
        elif args.delete[0] == 'Taille':
            print(find_by_taille(s, dbtable, args.delete[1], 'del'))
        elif args.delete[0] == 'Type':
            print(find_by_type(s, dbtable, args.delete[1], 'del'))
        else:
            print('invalid search: ' + args.delete[1])

    if args.modify:
        if args.modify[1] == 'Nom':
            modify_name_by_id(s, dbtable, int(args.modify[0]), args.modify[2])
        elif args.modify[1] == 'Description':
            modify_description_by_id(s, dbtable, int(args.modify[0]), args.modify[2])
        elif args.modify[1] == 'Taille':
            modify_taille_by_id(s, dbtable, int(args.modify[0]), args.modify[2])
        elif args.modify[1] == 'Type':
            modify_type_by_id(s, dbtable, int(args.modify[0]), args.modify[2])
        else:
            print('invalid search: ' + args.delete[1])

    s.close()


