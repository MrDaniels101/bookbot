
import sys
from stats import text_count, count_chars, sorted_chars

def get_book_text(path_to_book):
    with open(path_to_book, 'r') as f:
        return f.read()

def main():
    path_to_book = path_from_cli
    text = get_book_text(path_to_book)
    num_words = text_count(text)
    char_counts = count_chars(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------") 
    sorted_list = sorted_chars(char_counts)
    for item in sorted_list:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path_from_cli = sys.argv[1]
with open(path_from_cli, 'r') as f:
    text = f.read()

main()