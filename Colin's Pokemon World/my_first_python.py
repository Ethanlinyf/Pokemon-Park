""" Hello world """

def sum_up():
    sum = 0 
    for i in range(1, 101):
        print(i)
        sum = sum + i

    return sum

    

def hello_world():
    print("Hello World")

def main():
    hello_world()
    print(sum_up())

if __name__ == "__main__":
    main()

    