#example1
# count=0
# while count<5:
#     print(count)
#     count+=1

#example2 "continue"

# for i in range(1,5):
#     if i==3:
#         continue
#         print(i)

#example3 "forelse"

# for num in range(5):
#     if num==3:
#         print("3 number is found")
#         break
# else:
#      print("not found in range")

#example 4 "Check the given number is prime or composite"

# Function to check if a number is prime
def is_prime(number):
    # 0 and 1 are not prime numbers
    if number <= 1:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


user_input = int(input("Enter a number: "))

# Check if the input number is prime
if is_prime(user_input):
    print(f"{user_input} is a prime number.")
else:
    print(f"{user_input} is a composite number.")
