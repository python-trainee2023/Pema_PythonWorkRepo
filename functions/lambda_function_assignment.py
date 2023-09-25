#take the input for the start and stop value for a range.
# Then get the sum of odd and even numbers within that range using function or lambda and display that.
def sum_even_numbers(start, stop):
    even_sum = 0
    for num in range(start, stop + 1):
        if num % 2 == 0:
            even_sum += num
    return even_sum

# odd no in range
sum_odd_numbers = lambda start, stop: sum(num for num in range(start, stop + 1) if num % 2 != 0)

#user input for the range
start = int(input("Enter the start value: "))
stop = int(input("Enter the stop value: "))
#even no display
even_result = sum_even_numbers(start, stop)
print(f"Sum of even numbers from {start} to {stop}: {even_result}")

#odd no
odd_result = sum_odd_numbers(start, stop)
print(f"Sum of odd numbers from {start} to {stop}: {odd_result}")
