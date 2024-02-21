def main():
    book_path = "books/frankenstein.txt"
    text = get_book(book_path)
    count = word_count(text)
    char_dict = letter_count(text)
    chars_sorted_list = letter_sort(char_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{count} words found in the document")
    print()

    for item in chars_sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

def word_count(text):
    words = text.split()
    return len(words)

def letter_count(text):
    count = {}
    lower = text.lower()
    for l in lower:
        if l in count:
            count[l] += 1
        elif l.isalpha():
            count[l] = 1
    return count



def sort_on(d):
    return d["num"]

def letter_sort(count):
    sorted_list = []
    for ch in count:
        sorted_list.append({"char": ch, "num": count[ch]})
    sorted_list.sort(reverse=True, key=lambda l : l["num"])
    return sorted_list



def get_book(path):
    with open(path) as f:
        return f.read()


main()

