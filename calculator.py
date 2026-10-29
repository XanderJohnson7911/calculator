#SCCM4910 lab project. A four operation calculator


def add(a, b):
	return a+b

def subtract(a, b):
	return a-b

def multiply(a, b):
	return a*b

def divde(a, b):
	return a/b

def main():
	while True:
		a=float(input("First number: "))
		op=input("Operator (+ - * /): ")
		b=float(input("Second number: "))
		if op=="+":
			print("Result : ", add(a, b))
		elif op=="-":
			print("Result : ", subtract(a, b))
		elif op=="*":
			print("Result : ", multiply(a, b))
		elif op=="/" and b==0:
			print("Error, cannot divide by 0")
		elif op=="/":
			print("Result : ", divde(a, b))
		else:
			print("Unknown Operator : ", op)

if __name__ == "__main__":
	main()

