#example1:
# a=33
# b=33
# if b>a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")

#example2
# x=15
# if x<10:
#     print(x ,"is less than 10")
# elif x>10:
#     print(x,"is greater than 10")

# example3 palindrome string check

def is_palindrome(s):

    s = s.replace(" ", "").lower()

    # Check if the string is equal to its reverse
    if s == s[::-1]:
        return True
    else:
        return False



user_input = input("Enter a string: ")

# Check if the input is a palindrome
if is_palindrome(user_input):
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")


