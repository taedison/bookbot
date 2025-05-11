def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    text_list = text.split()
    text_num = 0
    for words in text_list:
        text_num += 1
    return text_num

def main():
    booktext = get_book_text("books/frankenstein.txt")
    num_words = count_words(booktext)
    print(f"{num_words} words found in the document")

main()