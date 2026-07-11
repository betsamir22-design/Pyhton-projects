
library=[]
wishlist=[]
book_name=input("Enter the name of book you own :")
library.append(book_name)
anothe_book_name=input("Enter the name of another book you have or press \"Enter\" to skip :")
if another_book_name:
    library.append(another_book_name)
    
print("Your library is :",library)
wishlist_book=input("Enetr the name of book you want to have :")
wishlist.append(wishlist_book)
another_wishlist_book=input("Enter the name of another book you want to have or press \"Enter\" to skip:")
if another_wishlist_book:
    wishlist.append(another_wishlist_book)
print("your wishlist is :",wishlist)

new_book=input("Enter the name of a book you have acquired or press \"Enter\" to skip :")
if new_book in wishlist:
    wishlist.remove(new_book)
    library.append(new_book)
    
print("\n uptaded library :",library)
print(" updated wishlist :",wishlist)

donated_book=input("Enter the name of book that you want to donate or press \"Enter\" to skip :")
if donated_book in library:
    library.remove(donated_book)
print("Your final library is :",library)