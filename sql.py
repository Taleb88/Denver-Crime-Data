import psycopg2

conn = psycopg2.connect(database='denver_crime_rate',
                        user='postgres', password='root',
                        host='127.0.0.1', port='5432'

)

conn.autocommit = True
cursor = conn.cursor()

if conn:
    print('db connection = success')

sql = ''''''