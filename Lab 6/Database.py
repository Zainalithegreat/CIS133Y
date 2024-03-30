class Database:

  @classmethod
  def readNames(cls):
    return [{
        "name": "John",
        "year": 1915,
        "gender": "M",
        "count": 47577
    }, {
        "name": "John",
        "year": 1916,
        "gender": "M",
        "count": 50046
    }, {
        "name": "John",
        "year": 1917,
        "gender": "M",
        "count": 51851
    }, {
        "name": "John",
        "year": 1918,
        "gender": "M",
        "count": 56559
    }, {
        "name": "John",
        "year": 1919,
        "gender": "M",
        "count": 53532
    }]
  classmethod
  def connect(cls):
      if cls.__connection is None:
        cls.__connection = pymssql.connect(server='cisdbss.pcc.edu', user='275student', password='275student', database='NAMES')

#54

