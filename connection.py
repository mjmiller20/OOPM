import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            host="54.237.205.175",
            database="testdb",
            user="postgres",
            password="FSd0\\0*K<PTNEwhg^SUaM6&6")
        
        cur = conn.cursor()
        cur.execute('SELECT * from Car;')
        result =  cur.fetchall()
        print(result)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    connect()
