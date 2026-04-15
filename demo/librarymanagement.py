books_list = []
authors_set = set()
books_dict = {}

books_list.append("python programing")
authors_set.add("john smith")
books_dict["python programing"] = "john smith"

books_list.append("python fundamentals")
authors_set.add("john smith")
books_dict["python fundamentsls"] = "john smith"

books_list.append("data structures and algorithms")
authors_set.add("jane doe")
books_dict["data structures and algorithms"] = "jane doe"

books_list.append("machine learning basics")
authors_set.add("alice johnson")
books_dict["machine learning basics"] = "alice johnson"

search_title = input("enter the title of the book to to search:")
if search_title in books_list:
    print(f"book found! the author of the book {search_title} is {books_dict [search_title]}")
else:
    print("book not found!")

remove_title = input("enter the title of the book to remove or else enter to skip: ")
if remove_title in books_list:
    remove_author = books_dict[remove_title]
    books_list.remove(remove_title)
    del books_dict[remove_title]

    if remove_author not in books_dict.values(): #check if the author has any other books in the dictionary
        authors_set.remove(remove_author)

    print("books removed succesfully!")
    print("books available along wiht their authors: ", books_dict)
    print("just available books:", books_list)
    print("just availabe authors:", authors_set)

else:
    print("book not found!")