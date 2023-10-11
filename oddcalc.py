first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("What kind of operation do you want to do? (mul, div, mod): ")

if operation == "mul":
    print("Result:", first_number * second_number)
elif operation == "div":
    print("Result:", first_number / second_number)
elif operation == "mod":
    print("Result:", first_number % second_number)
else:
    print(" *** invalid operation *** ")