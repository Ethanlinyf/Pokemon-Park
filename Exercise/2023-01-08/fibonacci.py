''' 
Something Good as Indicated by ...

To create a Fibonacci Sequence
'''


def welcome_message():
	print("Welcom to this Python program")
    

def fibo_seq(n):
	fib = [0, 1]

	if n == 1: 
		return [0]
	elif n == 2: 
		return fib
	elif n > 2:
		for i in range(n-2):
			fib.append(fib[i] + fib[i+1])

		return fib


def main():
	welcome_message()

	n = int(input("Please input a number: "))

	print(fibo_seq(n))


if __name__ == "__main__":
	main()

main()
