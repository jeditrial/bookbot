import sys
from stats import get_num_words, get_char_count, sorted_count


def get_book_text(file_input):
    with open(file_input) as f:
        file_contents = f.read()
    return str(file_contents)

def main():
    if len(sys.argv) > 1:
        text = get_book_text(sys.argv[1]) #get_book_text("books/frankenstein.txt")
        number_of_words = get_num_words(text)
        unique_char_count = get_char_count(text)
        sorted = sorted_count(unique_char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {sys.argv[1]}")
        print("----------- Word Count ----------")
        print(f"Found {number_of_words} total words")
        print("--------- Character Count -------")
        for key,value in sorted.items():
            if key.isalpha():
                print(f"{key}: {value}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()