class Book:
    def __init__(self,title,author,pages,year,genre,bookmark):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year
        self.genre = genre
        self.bookmark = bookmark
    def pageNum(self):
        return self.bookmark
    #Allows class to be converted to a string
    def __str__(self):
        return f"{self.title} was written by {self.author} in {self.year} and is a {self.pages} page long, {self.genre} story"
    #This allows the class to be printed even if the object is in another object
    def __repr__(self):
        #return self.__str__()
        return f"{self.title},{self.author},{self.year}"
book1 = Book("Expiditionary Force", "Craig Allanson", 724, 2013, "Science-Fiction/Action", 468)
book2 = Book("Harry Potter", "J.K Rowling", 1000, 2001, "Fantasy", 212)
library = [book1,book2]
print(book1)
print(book1.pageNum())
print(library)


