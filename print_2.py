

class ECC:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

def hello_world(name):
    print("Hello %s, welcome to the python World!" % (name))


def main():
    Junyu = ECC("Junyu", 10, "M")
    Junhao = ECC("Junhao", 12, "M")
    Jason = ECC("Jason", 11, "M")
    Joshua = ECC("Joshua", 13, "M")
    Colin = ECC("Colin", 12, "M")

    hello_world(Junyu.name)

if __name__ == "__main__":
    main()


