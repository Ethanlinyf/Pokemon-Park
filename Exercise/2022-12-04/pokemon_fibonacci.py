'''
Something good as indicated by Colin, Jason, Junyu, Junhao

'''

class Pokemon:
    fibo_list = [0, 1]
    def __init__(self, name, age, typee, level, agility, strength, intelligence):
        self.name = name
        self.age = age
        self.typee = typee
        self.level = level
        self.agility = agility
        self.strength = strength
        self.intelligence = intelligence
        self.health = level * strength # new attribute not from import. 

    def display(self):
        pokemon_dic = {
            'Name' : self.name,
            'Level' : self.level,
            'Strength' : self.strength,
            'Health' : self.health
        }

        for key, value in pokemon_dic.items():
            print(key, ':', value)

    def generate_fibo_list(self, n):
        n1 = 0
        n2 = 1

        for i in range(n-2):
            temp = n1
            n1 = n2 
            n2 = temp + n2
            self.fibo_list.append(n2)

            i = i + 1

        print(self.fibo_list)


def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return recur_fibo(n-1) + recur_fibo(n-2) 


def main():
    eevee = Pokemon("Eevee", 8, "Grass", 10, 12, 100, 80)

    eevee.display()
    
    n = int(input("Please input your number of items you want to genenrate: "))
    eevee.generate_fibo_list(n)

    print(recur_fibo(n-1))


if __name__ == "__main__":
    main()



        