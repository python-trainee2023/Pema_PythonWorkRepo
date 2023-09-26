def search_books_by_author(author_name, file_name):
    try:
        with open(file_name,'r') as file:
            matching_books = []
            for line in file:
                fields = line.strip().split(', ')
                if len(fields) == 3 and fields[1] == author_name:
                    matching_books.append(fields)

            if matching_books:
                print("Books by {}: \n".format(author_name))
                for book in matching_books:
                    print("Title: {}\nAuthor: {}\nYear: {}\n".format(book[0], book[1], book[2]))
            else:
                print("No books found by author: {}".format(author_name))

    except FileNotFoundError:
        print("File '{}' not found.".format(file_name))
    except Exception as e:
        print("An error occurred:", e)

def main():
    file_name = "book.txt"
    author_name = input("Enter the author's name: ")
    search_books_by_author(author_name, file_name)

if __name__ == "__main__":
    main()
