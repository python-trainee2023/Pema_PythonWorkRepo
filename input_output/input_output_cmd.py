import sys

#checkingif at least one arg is provided
if len(sys.argv) < 2:
    print("usage: python script.py <user_input>")
else:
    user_input = sys.argv[1]
    print("you entered:", user_input)