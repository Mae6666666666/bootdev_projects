def get_num_words(path):
    total_words = 0
    with open(path) as f:
        readable_book = f.read()
        split_words = readable_book.split()
        for word in split_words:
            total_words += 1
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")
# get_num_words()

def character_frequency(path):
    character_dic = {}
    with open(path) as f:
        readable_book = f.read()
        no_uppercase_book = readable_book.lower()
        for letter in no_uppercase_book:
            if letter not in character_dic:
                character_dic[letter] = 0
            character_dic[letter] += 1
        print(character_dic)
# character_frequency()

def sorted_dictionary_list(path):
    # list_for_dictionary = []
    # list_for_dictionary.append(character_dic)
    character_dic = {}
    with open(path) as f:
        readable_book = f.read()
        no_uppercase_book = readable_book.lower()
        for letter in no_uppercase_book:
            if letter != " ":
                if letter not in character_dic:
                    character_dic[letter] = 0
                character_dic[letter] += 1
        
    sorted_items = sorted(character_dic.items(), key=lambda item: item[1], reverse=True)

    for key, value in sorted_items:
        print(f"{key}: {value}")
# sorted_dictionary_list()

