import mysql.connector
import uuid
from mysql.connector import errorcode
from sqlalchemy.sql import text

# Obtain connection string information from the portal
config = {
    'host': 'hans-db.mysql.database.azure.com',
    'user': 'hans@hans-db',
    'password': 'han6113!',
    'database': 'samplez',
    'client_flags': [True],
    # 'ssl_cert': '/var/wwww/html/DigiCertGlobalRootG2.crt.pem'
}

class Connector:
    conn = None

    def __init__(self, connect_info=None):
        if self.conn is None:
            try:
                conn = mysql.connector.connect(**config)
                print("Connection established")
            except mysql.connector.Error as err:
                if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                    print("Something is wrong with the user name or password")
                elif err.errno == errorcode.ER_BAD_DB_ERROR:
                    print("Database does not exist")
                else:
                    print(err)
            else:
                self.conn = conn

    def __enter__(self):
        # self.conn = engine.connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()


def select_data(sql, data={}):
    with Connector() as conn:
        cur = conn.cursor()
        cur.execute(sql, data)
        return cur.fetchall()


def insert_data(sql, data):
    with Connector() as conn:
        cur = conn.cursor()

        try:
            for line in data:
                cur.execute(sql, line)

            conn.commit()
        except Exception as ex:
            conn.rollback()
        finally:
            conn.close()


if __name__ == '__main__':
    # statement = "INSERT INTO `tet` (`aa`, `bb`) VALUES (%(aa)s, %(bb)s)"
    # data = ({'aa': '102', 'bb': 103},
    #         # {'name': 'aa', 'quantity': 22},
    #         )
    # insert_data(statement, data)

    s_sql = "select * from tet where aa like %(aa)s"
    s_sql = "select * from ot_col_rule_dtl"
    s_data = {'aa': '101%'}
    s_data = {}
    result = select_data(s_sql, s_data)
    print('count : ' + str(len(result)))
    print(result)


# Construct connection string
# try:
#     conn = mysql.connector.connect(**config)
#     print("Connection established")
# except mysql.connector.Error as err:
#     if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
#         print("Something is wrong with the user name or password")
#     elif err.errno == errorcode.ER_BAD_DB_ERROR:
#         print("Database does not exist")
#     else:
#         print(err)
# else:
#
#     cursor = conn.cursor()
#
#     try:
#         # Drop previous table of same name if one exists
#         cursor.execute("DROP TABLE IF EXISTS inventory;")
#
#         # Create table
#         cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
#
#         # Insert some data into table
#         cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
#         cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
#         cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
#
#         conn.commit()
#     except Exception as ex:
#         print(ex)
#     finally:
#         cursor.close()
#         conn.close()
#
#     print("Done.")
