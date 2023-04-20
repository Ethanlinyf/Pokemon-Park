"""

"""


class Person:
    
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def print_name(self):
        print(self.fname, self.lname)


# pure inheritance
class Student(Person):
  pass



# case 1
class Student1(Person):
  def __init__(self, fname, lname):
      self.fname = fname
      self.lname = lname
class Student2(Person):
    super().__init__(fname, lname)

class Student3(Person):
    def __init__(self, fname, lname):
        super().__init__(fname, lname)

# case 2: add properties
class Student(Person):
  def __init__(self, fname, lname):
    super().__init__(fname, lname)
    self.graduationyear = 2019

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname,  self.lastname, "to the class of", self.graduationyear)
        
def main():
    p1 = Person('John', 'Doe')
    p1.print_name()

    s1 = Student('Jason', 'Young')
    s1.print_name()

if __name__ == '__main__':
    main()

