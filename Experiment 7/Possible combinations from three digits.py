digits = input().split()
a, b, c= digits
combinations = [
	a + b + c,
	a + c + b, 
	b + a + c, 
	b + c + a, 
	c + a + b, 
	c + b + a
]
for combo in combinations:
	print(combo)
