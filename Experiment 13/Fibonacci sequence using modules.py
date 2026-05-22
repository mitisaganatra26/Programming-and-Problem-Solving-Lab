# Read the number of operations
n_str = input().strip()
if n_str:
    n = int(n_str)
else:
    n = 0

# Initialize the phone database
phone_book = {}

for _ in range(n):
    # Read the operation line and split it into parts
    line = input().split()
    if not line:
        continue
        
    command = line[0]

    if command == "ADD":
        # ADD <name> <phone_number>
        name = line[1]
        phone = line[2]
        # This updates the number if the name already exists, 
        # or adds it if it doesn't.
        phone_book[name] = phone

    elif command == "REMOVE":
        # REMOVE <name>
        name = line[1]
        # Use .pop() with None to ignore the operation if name doesn't exist
        phone_book.pop(name, None)

    elif command == "DISPLAY":
        if not phone_book:
            print("No contacts")
        else:
            # Sort the names (keys) alphabetically
            sorted_names = sorted(phone_book.keys())
            for name in sorted_names:
                print(f"{name}: {phone_book[name]}")
