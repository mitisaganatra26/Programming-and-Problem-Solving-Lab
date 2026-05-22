def sum_of_digits_recursive(n):
	if n<10:
		return n
	else:
		last_digit = n% 10
		remaining_part = n//10
		
	
	
	return last_digit + sum_of_digits_recursive(remaining_part)



number = int(input())

result = sum_of_digits_recursive(number)	
print(result)

	
