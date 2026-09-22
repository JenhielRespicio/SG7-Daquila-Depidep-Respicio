try: # To execute valid input and its ranges
    age = int(input("What is your age? "))

    if 18 >= age >= 12: # Processes input age with range to output validity
        print("Valid age.")
    else: # To display invalidity because it is outside the scope of range
        print("Invalid age. Age must be from 12 to 18.")

except ValueError: # Backup code in case of the data type is invalid
    print("Invalid input. Please enter a whole number.")
