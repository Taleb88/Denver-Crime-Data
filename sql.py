import psycopg2

conn = psycopg2.connect(database='denver_crime_rate',
                        user='postgres', password='root',
                        host='127.0.0.1', port='5432'

)

conn.autocommit = True
cursor = conn.cursor()

if conn:
    print('db connection = success')

create_table = '''CREATE TABLE crime(
            incident_id BIGINT,
            offense_id CHAR(50),
            offense_code INT,
            offense_code_extension INT,
            offense_type_id CHAR(50),
            offense_category_id CHAR(50),
            first_occurrence_date CHAR(25),
            last_occurrence_date CHAR(25),
            reported_date CHAR(25),
            incident_address CHAR(150),
            geo_x CHAR(25),
            geo_y CHAR(25),
            geo_lon CHAR(25),
            geo_lat CHAR(25),
            district_id CHAR(25),
            precinct_id INT,
            neighborhood_id CHAR(50),
            is_crime INT,
            is_traffic INT,
            victim_count INT);'''

cursor.execute(create_table)

if cursor:
    print('successfully created table')

ingest_data = '''COPY crime(
                incident_id,
                offense_id,
                offense_code,
                offense_code_extension,
                offense_type_id,
                offense_category_id,
                first_occurrence_date,
                last_occurrence_date,
                reported_date,
                incident_address,
                geo_x,
                geo_y,
                geo_lon,
                geo_lat,
                district_id,
                precinct_id,
                neighborhood_id,
                is_crime,
                is_traffic,
                victim_count)
                FROM 
                DELIMITER ','
                CSV HEADER;'''

cursor.execute(ingest_data)

if cursor:
    print('successfully ingested data')

#select_all = '''select * from crime;'''
#cursor.execute(select_all)
#for x in cursor.fetchall():
    #print(x)

conn.commit()
conn.close()