# ip_str = input("Enter multiple values separated by space: ")
# list_val = ip_str.split()
#
# integers = []
# strings = []
#
# for item in list_val:
#     if item.isdigit():
#         integers.append(int(item))
#     else:
#         strings.append(item)
#
# print("Strings:", strings)
# print("Integers:", integers)
user_input = input("Enter multiple values seperated by a comma: ")

values = user_input.split(",")

int_list = []

float_list = []

string_list = []

for value in values:

    try:
        int_value = int(value)
        int_list.append(int_value)
    except ValueError:

        try:
            float_value = float(value)
            float_list.append(float_value)
        except ValueError:

            string_list.append(value)

print("Integer list: ", int_list)

print("Float list: ", float_list)

print("String list: ", string_list)