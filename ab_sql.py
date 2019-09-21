import psycopg2
# try:
#     conn = psycopg2.connect(dbname='test', user='postgres3', 
#                         password='root', host='localhost')
# except OperationalError:
#     print('Ошибка подключения')

conn = psycopg2.connect(dbname='test', user='postgres', 
                         password='root', host='localhost')
print(conn)
cursor = conn.cursor()