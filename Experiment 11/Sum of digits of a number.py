num = int(input("Enter a number: "))
digit_sum = 0
n = abs(num)
while n>0:
	digit = n% 10
	digit_sum += digit 
	n = n// 10



print("Sum of digits:",  digit_sum   )
