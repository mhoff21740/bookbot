
def get_book_text(book):
    book_text= f"books/{book}"
    with open(book_text) as f:
        text = f.read()
    return text


def get_letter_count(book):
    letter_dict={}
    book_text= get_book_text(book)
    sanitize_text= book_text.lower()
    for letter in sanitize_text:
        if letter in letter_dict:
            letter_dict[letter] += 1
        else:
            letter_dict[letter] = 1
    return letter_dict



def get_book_words(book):
    book_text = get_book_text(book)
    words = book_text.split()
    return len(words)

def sort_on(letter_dict):
    sorted_dict = []
    for letter in letter_dict:
        if letter.isalpha():
            sorted_dict.append({"char": letter, "num" : letter_dict[letter]})
    sorted_dict.sort(key = lambda item: item["num"], reverse=True)
    return sorted_dict
    
    



def final_report(book):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book}")
    print("----------- Word Count ----------")
    print(f"Found {get_book_words(book)} total words")
    print("--------- Character Count -------")
    letter_dict = get_letter_count(book)
    sorted_characters = sort_on(letter_dict)
    for item in sorted_characters:
        print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")
