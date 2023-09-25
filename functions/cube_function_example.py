#display cube using function
def cube(num):
    return num ** 3

user_input = input("Enter a number: ")

try:
    num = float(user_input)

    result = cube(num)

    print(f"The cube of {num} is {result}")
except ValueError:
    print("Invalid input. Please enter a valid number.")
