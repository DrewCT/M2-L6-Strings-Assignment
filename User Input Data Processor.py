def input_length_validator():
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()

    if len(first_name) < 2:
        print("Error: First name must be at least 2 cjharacters long.")
    else:
        print("First name is valid.")
    
    if len(last_name) < 2:
        print("Error: Last name must be at least 2 characters long.")
    else:
        print("Last name is valid.")

input_length_validator()