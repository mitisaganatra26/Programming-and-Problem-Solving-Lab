try:
	marks = list(map(int, input().split()))
	if len(marks)==4:
		total_marks = sum(marks)
		aggregate = total_marks/4
		if aggregate > 75:
			grade = "Distinction"
		elif aggregate >= 60:
			grade = "First Division"
		elif aggregate >= 50:
			grade = "Second Division"
		elif aggregate >= 40:
			grade = "Third Division"
		else:
			grade = "Fail"
		print(total_marks)
		print(f"{aggregate:.2f}")
		print(grade)
	else:
		print("Please enter exactly four marks.")
except ValueError:
	print("Invalid input. Please enter integers only.")
	
