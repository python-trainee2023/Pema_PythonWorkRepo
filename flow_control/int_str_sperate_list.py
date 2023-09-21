ip_str = input("Enter multiple values separated by space: ")
list_val = ip_str.split()

integers = []
strings = []

for item in list_val:
    if item.isdigit():
        integers.append(int(item))
    else:
        strings.append(item)

print("Strings:", strings)
print("Integers:", integers)
