class Student:
  def __init__(self, name, age, grade=1):
    self.age = age
    self.name = name
    self.grade = grade

  def printStudentInfo(self):
    print(self.name + " " + str(self.grade))

blake = Student("Blake", 10, 5);
matthew = Student("Matthew", 16, 11);
aj = Student("AJ", 13, 8);
ridwan = Student("Ridwan", 15)

ridwan.printStudentInfo()