import sys
from stats import count_words
from stats import count_characters
from stats import sort_dict

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    booktext = get_book_text(path)
    num_words = count_words(booktext)
    characters = count_characters(booktext)
  

    sorted = sort_dict(characters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for keys in sorted: # iterate over list
        if keys["char"].isalpha():
            charact = keys["char"]
            number = keys["num"]
            print(f"{charact}: {number}")
    print("============= END ===============")

main()