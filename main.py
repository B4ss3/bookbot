from stats import count_words, count_characters, sort_dictionary, get_available_books
import sys
def main():
 
    if len(sys.argv) != 2:
        print("Usage: python3 main.py books/ <book name>")
        print(get_available_books())
        sys.exit(1)
    book_path = sys.argv[1]

    text = get_book_text(book_path)
    word_count = count_words(text)
    chars_dict = count_characters(text)
    sorted_dict = sort_dictionary(chars_dict)
    print_report(book_path,word_count, sorted_dict)



def print_report(book_path, word_count, sorted_dict):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}")
    print(f"----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for char in sorted_dict:
        if char.isalpha() == True:
            print (f"{char}: {sorted_dict[char]}")
    print("============= END ===============")
    

def get_book_text(path):
    with open(path) as f:
        return f.read()

    

main()



