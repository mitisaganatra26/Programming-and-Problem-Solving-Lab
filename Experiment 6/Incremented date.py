def is_leap(year):
	return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def get_next_date():
	try:
		day = int(input())
		month = int(input())
		year = int(input())
		if year <= 0 or month < 1 or month >12:
			print("Invalid Date")
			return
		if month in[1, 3, 5, 7, 8, 10, 12]:
			max_days = 31
		elif month in[4, 6, 9, 11]:
			max_days = 30
		elif month == 2:
			max_days = 29 if is_leap(year) else 28
		if day < 1 or day > max_days:
			print("Invalid Date")
			return
		if day< max_days:
			day += 1
		else:
			day = 1
			if month == 12:
				month = 1
				year += 1
			else:
				month += 1
		print(f"{day:02d}-{month:02d}-{year}")
	except EOFError:
		pass
	except ValueError:
		print("Invalid Date")
if __name__ == "__main__":
	get_next_date()
