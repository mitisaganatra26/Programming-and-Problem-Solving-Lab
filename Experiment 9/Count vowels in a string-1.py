# Read the input string
text = input()

# Define the vowels (lowercase)
vowels = "aeiou"

# Initialize a counter
vowel_count = 0

# Loop through each character in the string
for char in text:
    # Convert character to lowercase and check if it's a vowel
    if char.lower() in vowels:
        vowel_count += 1

# Print the final result
print(vowel_count)
