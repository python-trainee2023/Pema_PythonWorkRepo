#print even only using list comprehension classwork1
# number_list = [2, 4, 5, 9, 18, 20]
# filtered_list = [x for x in number_list if x % 2 == 0]
# print(filtered_list)

#priya's error
# numbers[2,4,5,9,18,20]
#
# result_List=[]
# for num in numbers:
#     if num%2 == 0:
#         result_List.append(num)
#         numbers =result_List
#     print(numbers)
#
#     numbers = [2, 4, 5, 9, 18, 20]
#     result_List = []

#priya's error resolve
# numbers = [2, 4, 5, 9, 18, 20]
# result_List = []
#
# for num in numbers:
#     if num % 2 == 0:
#         result_List.append(num)
#
# numbers = result_List
#
# print(numbers)

# num_list=list(range(1,10))
# print(num_list)
# square=[x ** 2 for x in num_list]
# print(square)
#
# fruits=["apple", "kiwi", "banana"]
# upper_case_fruits=[fruits.upper() for x in fruits]
# print(upper_case_fruits)

#to print integers only and remove floating-point Classwork 2
# num = [1, 2, 3, 4.5, 6, 7.2]
#
# integers_only = [x for x in num if isinstance(x, int)]
#
# print(integers_only)


# Input three numbers from the user classwork3
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

#to find the maximum
maximum = max([number1, number2, number3])

# Print the max no
print("The maximum number is:", maximum)

#rejan's with sorting
# user_input = input('Enter 3 numbers')
# input_list = list(user_input.split(','))
#
# num_list = [int(x) for x in input_list]
#
# num_list.sort()
#
#
# print(num_list[len(num_list)-1])


