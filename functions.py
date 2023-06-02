import json
from models import Publisher, Shop, Book, Stock, Sale


def fill_in_the_tables(session):
    try:
        with open('fixtures/tests_data.json', 'r') as fd:
            data = json.load(fd)
        for record in data:
            model = {
                'publisher': Publisher,
                'shop': Shop,
                'book': Book,
                'stock': Stock,
                'sale': Sale,
            }[record.get('model')]
            session.add(model(id=record.get('pk'), **record.get('fields')))
        session.commit()
    except Exception as _ex:
        print('Данные уже были записаны в базу данных!')
        session.close()
    else:
        print('Данные успешно записаны!')


def search_by_publisher(search_publisher, session):
    for book_name, shop_name, price, date_sale in session.query(Book.title, Shop.name, Sale.price, Sale.date_sale)\
            .join(Publisher).join(Stock).join(Shop).join(Sale).filter(Publisher.name == search_publisher).all():
        print(f'{book_name} | {shop_name} | {price} | {date_sale}')