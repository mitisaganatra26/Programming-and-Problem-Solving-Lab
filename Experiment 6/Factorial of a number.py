def calculate_factorial():
	try:
		n=int(input())
		if n<0:
			return
		factorial = 1
		for i in range(1, n+1):
			factorial *=i
		print(factorial)
	except ValueError:
		pass
if __name__ == "__main__":
	calculate_factorial()
