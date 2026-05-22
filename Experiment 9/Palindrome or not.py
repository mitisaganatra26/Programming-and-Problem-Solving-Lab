# Read the input string
text = input()

# Reverse the string using slicing [start:stop:step]
# Step -1 means it reads the string backwards
reversed_text = text[::-1]

# Check if the original string matches the reversed string
if text == reversed_text:
    print("Palindrome")
else:
    print("Not a Palindrome")
