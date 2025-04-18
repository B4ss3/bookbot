import os
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    lowered = text.lower()
    char_dict = {}

    for char in lowered:
        if char in char_dict:
            char_dict[char] = char_dict[char] + 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_dictionary(dct):

    sorting_dict = sorted(dct.items(), key=lambda kv: kv[1], reverse= True)
    return dict(sorting_dict)

def get_available_books():
    books = os.listdir("./books")
    return books