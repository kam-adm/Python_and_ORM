import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models import create_tables
from functions import fill_in_the_tables, search_by_publisher

user = ''
password = ''
name_db = ''

DSN = f'postgresql://{user}:{password}@localhost:5432/{name_db}'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()
print("""Для заполнения таблиц введите - 1
Для поиска по издателю введите - 2
Для выхода из программы введите - 3"""
      )
command = 0
while command != '3':
    command = input('Введите комманду: ')
    if command == '1':
        fill_in_the_tables(session)
    elif command == '2':
        search_publisher = input('Введите имя издателя: ')
        search_by_publisher(search_publisher, session)
    elif command == '3':
        print('Работа с программой завершена!')
    else:
        print('Вы ввели неверные данные!')


session.close()
