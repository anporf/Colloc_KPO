from mysql import connector


def make_connect():
    cnx = connector.connect(user='root',
                            password='aaaa',
                            host='localhost',
                            port=3306,
                            database='Colloc')
    return cnx


def get_from_db(query):
    cnx = make_connect()
    cnx.close()
    cnx.reconnect()
    cursor = cnx.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def change_on_db(query):
    cnx = make_connect()
    cnx.close()
    cnx.reconnect()
    cursor = cnx.cursor()
    cursor.execute(query)
    cnx.commit()