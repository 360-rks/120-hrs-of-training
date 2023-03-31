"""The central library at Mysore has a set of very interesting
 books and journals. The books are arranged in the 
alphabetical order of their author names. 
So it is very easy for the readers to search for the book.
The library has got a set of new books. The librarian wants
 to arrange them in order too. As some books are already 
arranged in the order, find a suitable way of arranging the 
new set of books amidst them.

Write a python program to arrange all the books in the 
alphabetical order of the author names.
sort_item_list_by_author(): Accepts the new list of books 
and returns it sorted in the alphabetical order of their 
author names.
add_new_items(): Accepts the new list of books, sorts it and
 merges it with the existing books in the library.
Hint - Use sort_item_list_by_author() method for sorting the 
books.
sort_items_by_published_year(): Sorts the list of books (item_list) based on the increasing order of their published years. If there are multiple items that
are published in the same year, then sort them based on the alphabetical order of their author names.
Note: While sorting the author names in alphabetical order, ignore the special characters including space, if there are any.

Library
- item_list
init(item_list)
+ get_item_list()
+ sort_item_list_by_author(new_item_list)
+ add_new_items(new_item_list)
+ sort_items_by_published_year()


Item
- item_name
- author_name
- published_year
init(item_name,author_name,published_year)
+ get_item_name()
+ get_author_name()
+ get_published_year()
str()"""
class books:
    def __init__(self,data):
        self.data=data
        self.nxt=None

class library:
    def __init__(self,item_list):
        self.head=None
        self.item_list=item_list
        if item_list:
            self.item_list=sorted(item_list,key=lambda x:x.author_name)
            
    def get_item_list(self):
        return self.item_list
    def sort_tem_list_by_author(self,new_item_list):
        item_list = self.get_item_list() + new_item_list
        item_list=sorted(item_list,key=lambda x:x.author_name)
        return item_list
        
    def add_new_items(self,new_item_list):
        if self.head is None:
            self.head=books(self.sort_tem_list_by_author(new_item_list))
        else:
            itr=self.head
            while itr.nxt:
                itr=itr.nxt
            itr.nxt=books(self.sort_tem_list_by_author(new_item_list))
        self.item_list = self.sort_items_by_published_year(self.get_item_list() + new_item_list)
    def sort_items_by_published_year(self,item_list):
        item_list=sorted(item_list,key=lambda x:x.published_year)
        return item_list
    def display_list(self):
        itr=self.head
        llstr=""
        while itr:
            llstr+=str(itr.data)+"--->"
            itr=itr.nxt
        print(llstr)

class Item:
    def __init__(self, item_name, author_name, published_year):
        self.item_name = item_name
        self.author_name = author_name
        self.published_year = published_year
    
    def get_item_name(self):
        return self.item_name
    
    def get_author_name(self):
        return self.author_name
    
    def get_published_year(self):
        return self.published_year
    
    def __str__(self):
        return f"{self.item_name} by {self.author_name}, published in {self.published_year}"


        

book1=Item("The Great Gatsby", "F. Scott Fitzgerald", 1925)
book2=Item("To Kill a Mockingbird", "Harper Lee", 1960)
book3=Item("Pride and Prejudice", "Jane Austen", 1813)
book4=Item("1984", "George Orwell", 1949)

lib=library([book1,book2])
print('\n'.join(map(str, lib.get_item_list())))

lib.add_new_items([book3,book4])
print("after adding new list")
print('\n'.join(map(str, lib.get_item_list())))