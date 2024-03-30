class Name:

  def __init__(self, name, year, gender, count):
    self.__name = name
    self.__year = year
    self.__gender = gender
    self.__count = count

  # Mutatorsany 
  def set_name(self, name):
    self.__name = name

  def set_year(self, year):
    self.__year = year

  def set_gender(self, gender):
    self.__gender = gender

  def set_count(self, count):
    self.__count = count

  # Accessors
  def get_name(self):
    return self.__name

  def get_year(self):
    return self.__year

  def get_gender(self):
    return self.__gender

  def get_count(self):
    return self.__count
