import sqlalchemy

host = 'localhost'
username = 'shinhan'
password = '1212'
port = '3306'
dbname = 'test'
conn_info = f"mysql+mysqldb://{username}:{password}@{host}/{dbname}"
engine = None


class Connector:
    con = None

    def __init__(self, connect_info=None):
        global engine
        if engine is None:
            # engine = create_engine(f"mysql+mysqldb://{username}:{password}@{host}/{dbname}", encoding='utf-8')
            engine = sqlalchemy.create_engine(
                connect_info, pool_size=5,
                max_overflow=5, pool_recycle=500)


    def __enter__(self):
        self.conn = engine.connect()
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.conn.close()

# class _Session():
#     session = None
#
#     def __init__(self, connect_info=None):
#         global engine
#         if engine is None:
#             engine = sqlalchemy.create_engine(
#                 connect_info, pool_size=5,
#                 max_overflow=5, pool_recycle=500)
#             Session.configure(bind=engine)
#
#     def __enter__(self):
#         self.session = Session()
#         print "enter = " + str(self.session)
#         return self.session
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is not None:
#             self.session.rollback()
#             print "rollback()" + str(self.session)
#         else:
#             self.session.commit()
#
#         print "close() : " + str(self.session)
#         self.session.close_all()
