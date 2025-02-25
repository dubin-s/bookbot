import sys
from stats import word_count
from stats import letter_count
from stats import sorted_content_count

def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
    return book_contents

def main():
    if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)

    filepath = sys.argv[1]
    content = get_book_text(filepath)
    wc = word_count(content)
    letters = letter_count(content)
    sorted_letters = sorted_content_count(letters)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}");
    print("----------- Word Count ----------")
    print(f"Found {wc} total words")
    print("--------- Character Count -------")
    for pair in sorted_letters:
        for key, value in pair.items():
            print(f"{key}: {value}")
    print("============= END ===============")
    return 0

main()