import psycopg2

def connect():
    try:
        conn = psycopg2.connect(
            host="52.204.130.69",
            database="projdb",
            user="projectadmin",
            password="FSd0\\0*K<PTNEwhg^SUaM6&6",
            port="5432")
        cur = conn.cursor()
        cur.execute('SELECT * from Car;')
        result =  cur.fetchall()
        print(result)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    connect()
