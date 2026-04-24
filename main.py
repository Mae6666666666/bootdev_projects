from stats import get_num_words
from stats import sorted_dictionary_list
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
book_path = sys.argv[1]
# print("*" * 50)
# print(book_path)
# print("*" * 50)
def get_book_text():
    with open(book_path) as f:
        print(f.read())

# get_book_text()
# print(sys.argv)


# print(len(sys.argv))


# print(sys.argv[0])


# print(sys.argv[1])

get_num_words(book_path)
sorted_dictionary_list(book_path)



