def word_count(content):
    return len(content.split())

def letter_count(content):
    chars = {}
    l_content = content.lower()
    for char in l_content:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars


def sorted_content_count(char_count):
    char_list = [{k : v} for k, v in char_count.items() if k.isalpha()]
    char_list.sort(reverse=True, key=lambda x: list(x.values())[0])
    return char_list