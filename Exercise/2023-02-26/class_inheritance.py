class Person():
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def display(self):
        print(self.fname, self.lname)


# Case 1: inheritance: Person 1

class Person1(Person):
    def __init__(self, fname, mname, lname):
        self.fname = fname
        self.mname = mname
        self.lname = lname

    def display(self):
        print(self.fname, self.mname, self.lname)

# Case 2: inheritance: Person 2 with age
class Person2(Person):
    def __init__(self, fname, lname, age):
        super().__init__(fname, lname)
        self.age = age

# Case 3: inheritance: Person 3 with a new function
class Person3(Person2):
    def display3(self):
        print(self.fname, self.lname, self.age)


def main():
    ethan = Person3('Ethan', 'Lin', 20)

    ethan.display3()

    
main()

if __name__ == "__main__":
    main()

