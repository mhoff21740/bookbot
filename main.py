

from stats import get_book_words



def main():
    book_text=get_book_words("frankenstein.txt")
    print (f"{book_text} words found in the document.")




main()


