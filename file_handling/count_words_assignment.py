def count_words_ending_with_e(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            count = 0

            for word in words:
                if word[-1].lower() == 'e':
                    count += 1
            return count

    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))
        return 0
    except Exception as e:
        print("An error occurred:", e)
        return 0

file_name = "textfile.txt"

with open(file_name, 'w') as sample_file:
    sample_file.write("apple orange grape banana\n")
    sample_file.write("tree house computer mouse\n")
    sample_file.write("book table chair laptop")

word_count = count_words_ending_with_e(file_name)
print("Number of words ending with 'e':", word_count)



