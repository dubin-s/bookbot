def sort_on(dict):
    return dict["num"]


def get_char_report(char_count):
    char_report = []
    for char in char_count:
        if char.isalpha():
            char_report.append({"char": char, "num": char_count[char]})
    char_report.sort(reverse=True, key=sort_on)
    return char_report


def get_char_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def get_num_words(text):
    return len(text.split())


def get_text(path):
    with open(path) as f:
        return f.read()


def main():
    file_path = "books/frankenstein.txt"
    text = get_text(file_path)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    char_report = get_char_report(char_count)

    print(f"--- Begin report of {file_path} ---")
    print(f"{num_words} words found in the document\n")
    for char in char_report:
        print(f"The \'{char["char"]}\' was found {char["num"]} times")
    print("--- End report ---")


main()
