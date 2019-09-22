#import psycopg2
# try:
#     conn = psycopg2.connect(dbname='test', user='postgres3', 
#                         password='root', host='localhost')
# except OperationalError:
#     print('Ошибка подключения')

# conn = psycopg2.connect(dbname='test', user='postgres', 
#                          password='root', host='localhost')
# print(conn)
# cursor = conn.cursor()

# from contextlib import closing
# with closing(psycopg2.connect(dbname='test', user='postgres', 
#                          password='root', host='localhost')) as conn:
#     with conn.cursor() as cursor:
#         cursor.execute('SELECT * FROM ab LIMIT 5')
#         for row in cursor:
#             print(row)


#https://eax.me/python-postgresql/
#https://pythonhosted.org/py-postgresql/
import postgresql
db = postgresql.open('pq://postgres:root@localhost:5432/test')

#СОЗДАНИЕ ТАБЛИЦЫ
# db.execute("CREATE TABLE users (id SERIAL PRIMARY KEY, "
#   "login CHAR(64), password CHAR(64))")

#ДОБАВЛЕНИЕ ЗАПИСЕЙ В ТАБЛИЦУ
# ins = db.prepare("INSERT INTO users (login, password) VALUES ($1, $2)")

# ins("vlad", "password")
# # ('INSERT', 1)
# ins("eax", "456")
# # ('INSERT', 1)

#ВЫВОД ЗАПИСЕЙ
qw  =   db.query("SELECT id, trim(login), trim(password) FROM users")
for item in qw:
    print(item)
    
# [(1, 'afiskon', '123'), (2, 'eax', '456')]

