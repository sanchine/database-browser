import pymysql

class Database:
    def __init__(self, db_name):
        self.host = "127.0.0.1"
        self.user = "root"
        self.password = "bb2w19dark228"
        self.port = 3306
        self.name = db_name
        self.connection = None

        try:
            self.connection = pymysql.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("Successfully connected!")
        except Exception as ex:
            print("Connection refused...")
            print(ex)

    def getTables(self):
        try:
            with self.connection.cursor() as cursor:
                show_table_query = "SHOW TABLES;"
                cursor.execute(show_table_query)
                data = cursor.fetchall()
                return data
        except Exception as ex:
            print("Getting tables refused..")
            print(ex)


    def getAbout(self, table_name):
        try:
            with self.connection.cursor() as cursor:
                data = []
                row_count_query = "SELECT COUNT(*) FROM {0};".format(table_name)
                cursor.execute(row_count_query)
                data.append(cursor.fetchall()[0]["COUNT(*)"])
                col_count_query = "SELECT COUNT(*) FROM information_schema.columns \
                                    WHERE table_name = '{0}' AND table_schema = '{1}'; \
                                    ".format(table_name, self.name)
                cursor.execute(col_count_query)
                data.append(cursor.fetchall()[0]["COUNT(*)"])
                return data
        except Exception as ex:
            print("Getting about refused..")
            print(ex)

    def getFieldsInfo(self, table_name):
        try:
            with self.connection.cursor() as cursor:
                fields_query = "SHOW fields FROM {0};".format(table_name)
                cursor.execute(fields_query)
                return cursor.fetchall()
        except Exception as ex:
            print("Getting about refused..")
            print(ex)

    def getTable(self, table_name):
        try:
            with self.connection.cursor() as cursor:
                fields_query = "SELECT * FROM {0};".format(table_name)
                cursor.execute(fields_query)
                return cursor.fetchall()
        except Exception as ex:
            print("Getting about refused..")
            print(ex)