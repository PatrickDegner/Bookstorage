from utils.database_connection  import DatabaseConnection


def create_book_table():
    with DatabaseConnection() as connection:
        cursor = connection.cursor()

        cursor.execute('create table if not exists books(name text,  author text, read integer)')


def add_book(name,author):
    with DatabaseConnection() as connection:
         cursor = connection.cursor()

         cursor.execute('insert into books (name, author, read) VALUES (%s,%s,0)',(name,author))


def get_all_books():
    with DatabaseConnection() as connection:
         cursor = connection.cursor()

         cursor.execute('Select * from books')
         books = [{'name': i[0], 'author': i[1], 'read': i[2]} for i in cursor.fetchall()]

         return books


def mark_book_as_read(name):
    with DatabaseConnection() as connection:
         cursor = connection.cursor()

         cursor.execute('update books set read=1 WHERE name=%s',(name,))


def delete_book(name):
    with DatabaseConnection() as connection:
         cursor = connection.cursor()

         cursor.execute('delete from books WHERE name = %s',(name,))
