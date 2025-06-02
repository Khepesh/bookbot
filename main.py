from stats import get_word_count, get_character_count

def get_book_text ( path ):
    with open(path) as f:
        return f.read()

def main ():
    book_path = "books/frankenstein.txt"

    book_content = get_book_text(book_path)
    word_count = get_word_count(book_content)
    character_count = get_character_count(book_content.lower())

    print(f"{word_count} words found in the document")
    print ("-------------------------------------")
    print("Character counts:")
    for char, count in character_count.items():
        print(f"'{char}': {count}")
    print("-------------------------------------")
    print("End of character counts")

main()