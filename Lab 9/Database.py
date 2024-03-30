import pymssql

class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
            cls.__connection = pymssql.connect(server='cisdbss.pcc.edu', user='275student', password='275student', database='NAMES')

    @classmethod
    def fetchNames(cls, name, gender):
        cls.connect()
        cursor = cls.__connection.cursor()
        sql = """
                SELECT Name, Year, Gender, NameCount, Total
                FROM all_data
                WHERE Name = %s
                AND Gender = %s
                ORDER BY Year;
               """
        cursor.execute(sql, (name, gender))
        rows = cursor.fetchall()
        return rows










