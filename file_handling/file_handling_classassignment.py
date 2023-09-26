with open('student.txt', 'r') as input_file, open('studentnew.txt', 'w') as output_file:

    for line in input_file:
        uppercase_line = line.upper()
        output_file.write(uppercase_line)

print("completed successfully.")
