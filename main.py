def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    character_count = get_character_count(text)
    character_list = convert_dictionary(character_count)
    character_list.sort(reverse=True, key=sort_on)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in this document")
    print("")
    for character in character_list:
        print(f"The '{character["name"]}' character was found {character["count"]} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def convert_dictionary(dic):
    chars = []
    for d in dic:
        char = {}
        char["name"] = d
        char["count"] = dic[d]
        if char["name"].isalpha() == True:
            chars.append(char)
    return chars

def sort_on(dict):
    return dict["count"]

def get_character_count(text):
    chars = {}
    for c in text.lower():
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

main()
