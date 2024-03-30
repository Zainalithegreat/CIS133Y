import pymssql

class Database:
    __connection = None

    @classmethod
    def connect(cls):
        if cls.__connection is None:
            cls.__connection = pymssql.connect(server='cisdbss.pcc.edu', user='275student', password='275student', database='NAMES')

    @classmethod
    def fetchNames(cls, year, gender):
        cls.connect()
        cursor = cls.__connection.cursor()
        sql = """
         SELECT TOP 50 Name, Year, Gender, NameCount
         FROM all_data
         WHERE Year = %s AND Gender = %s
        """
        cursor.execute(sql, (year, gender))
        rows = cursor.fetchall()
        return rows









