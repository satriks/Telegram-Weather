from sqlalchemy import Column, select
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String, create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import psycopg2
from sqlalchemy_utils import database_exists, create_database

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String(60), nullable=False)
    author = Column(String(30), nullable=False)
    reviews = relationship('Reviews',backref='book', lazy=True)

    def __repr__(self):
        return self.title

class Reviews(Base):
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True)
    text = Column(String(2000), nullable=False)
    book_id = Column(Integer, ForeignKey('books.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f'от {self.reviewer}'

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    reviews = relationship('Reviews', backref= 'reviewer', lazy=True)
    def __repr__(self):
        return self.name


if __name__ == '__main__':
    engine = create_engine('postgresql://postgres:123st321@localhost:5432/botwether', echo=False)

    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = select(Book).where(Book.title == 'Робинзон Крузо')
    for book in session.scalars(stmt):
        print(book, book.reviews, book.reviews[0].text)


    # добавление записей с БД
    '''
    engine = create_engine('postgresql://postgres:123st321@localhost:5432/botwether', echo=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    session.add(Book(title='Робинзон Крузо', author='Даниэль Дэфо'))  # Создаём книгу 1
    session.add(Book(title='Путешествие к центру земли', author='Жуль Верн'))  # Создаём книгу 2
    session.add(User(name='user1'))  # Пользователь 1
    session.add(User(name='user2'))  # Пользователь 2
    session.add(Reviews(text='Замечатьльный роман о приключениях Робинзона', book_id=1,
                        user_id=1))  # Отзыв о книге 1 от пользователя 1
    session.add(Reviews(text='Замечатьльный роман о путешествии к центру земли', book_id=2,
                        user_id=2))  # Отзыв о книге 2 от пользователя 2
    session.add(Reviews(text='Мне не понравилось', book_id=1, user_id=2))  # Отзыв о книге 1 от пользователя 2
    session.commit()'''





    # КОД СОЗДАНИЯ НОВОЙ БД (Надо устанавливать ! from sqlalchemy_utils import database_exists, create_database
    '''if not database_exists(engine.url):
        create_database(engine.url)

    print(database_exists(engine.url))

    Base.metadata.create_all(engine)'''

