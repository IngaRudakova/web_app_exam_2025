from models import db, User, Role, Book, Genre
from werkzeug.security import generate_password_hash
from app import app

with app.app_context():
    # Удаляем все существующие таблицы
    db.drop_all()
    # Создаем таблицы заново
    db.create_all()

    admin_role = Role(name='Администратор', description='Полный доступ')
    moder_role = Role(name='Модератор', description='Редактирование книг и рецензий')
    user_role = Role(name='Пользователь', description='Может оставлять рецензии')

    db.session.add_all([admin_role, moder_role, user_role])
    db.session.commit()

    users = [
        User(username='admin', password_hash=generate_password_hash('adminpass'),
             last_name='Волочкова', first_name='Анна', middle_name='Сергеевна', role=admin_role),
        User(username='mod', password_hash=generate_password_hash('modpass'),
             last_name='Москинов', first_name='Мод', middle_name='Москинович', role=moder_role),
        User(username='user', password_hash=generate_password_hash('userpass'),
             last_name='Юлаев', first_name='Юлий', middle_name='Борисов', role=user_role)
    ]
    db.session.add_all(users)

    genres = [Genre(name=name) for name in ['Фэнтези', 'Детектив', 'Роман', 'Исторический', 'Ужасы', 'Биография']]
    db.session.add_all(genres)
    db.session.commit()


    books = [
        Book(title='Властелин Колец', description='Эпическая сага о Средиземье и борьбе за Кольцо Всевластья.', year=1954, 
             publisher='Allen & Unwin', author='Дж. Р. Р. Толкин', pages=1178,
             genres=[genres[0], genres[3]]),
        Book(title='Шерлок Холмс: Собака Баскервилей', description='Знаменитый детектив о загадочных событиях в поместье Баскервилей.', year=1902,
             publisher='George Newnes', author='Артур Конан Дойл', pages=256,
             genres=[genres[1]]),
        Book(title='Дракула', description='Классический роман о вампирах и борьбе с ними.', year=1897,
             publisher='Archibald Constable and Company', author='Брэм Стокер', pages=418,
             genres=[genres[0], genres[4]]),
        Book(title='Анна Каренина', description='Трагическая история любви в высшем обществе России XIX века.', year=1877,
             publisher='Русский вестник', author='Лев Толстой', pages=864,
             genres=[genres[2], genres[3]]),     
        Book(title='Стив Джобс', description='Биография основателя Apple, написанная Уолтером Айзексоном.', year=2011,
             publisher='Simon & Schuster', author='Уолтер Айзексон', pages=656,
             genres=[genres[5]])         
    ]

    db.session.add_all(books)
    db.session.commit()
    print('✅ Пользователи, роли, жанры и книги успешно добавлены.')
