def factorial(num):
	if num==0:
		return 1  
	else:
		return num*factorial(num-1)  
value=int(input("Enter a number: "))
fact=factorial(value)
print("The factorial of",value,"is",fact)
