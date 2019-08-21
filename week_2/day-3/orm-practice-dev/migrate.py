import peeweedbevolve
from orm_practice_dev import db

if __name__ == '__main__':
   db.evolve(ignore_tables={'base_model'})