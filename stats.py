
def get_book_text(book):
    book_text= f"books/{book}"
    with open(book_text) as f:
        text = f.read()
    return text




def get_book_words(book):
    book_text = get_book_text(book)
    words = book_text.split()
    return len(words)
