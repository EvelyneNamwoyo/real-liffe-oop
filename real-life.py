#illustrating a scenario of students borrowing books from the library, 
#fining late delays, charging lost books
import datetime 
class Student(object):
    def __init__(self, name, idno,my_books=[], fines=[], books_returned=[]):
        self.my_books= my_books
        self.name = name
        self.idno = idno
        self.fines = fines
        self.books_returned = books_returned

class Book(object):
    def __init__(self, title, idno, price):
        self.title = title
        self.idno = idno
        self.price = price
class Librarian(object):
    def __init__(self, name, books_lent=[],library=[]):
        self.name=name
        self.books_lent = books_lent
        self.library =library

class Loan(object):
    def __init__(self, date_borrowed, date_returned):
        self.date_borrowed = date_borrowed
        self.date_returned = date_returned

if __name__ == "__main__":

    ann =Librarian("Ann khkjhkjlh")
    

    student_list=[]

    while True:
        choice=int(raw_input("1. Register student\n 2. Enter a book\n 3. Lend a book\n 4. Return a book\n 5. View list of books\n 6. students registered\n 7.Exit \nEnter choice [1-7]"))
        
        if (choice ==1):
            print ("Enter student details: ")
            name=raw_input("Name: ")
            idno=int(raw_input("IdNo: "))
            student=Student(name, idno)
            
            student_list.append(student)
            
            print("Student registered.")
            print([(y.name,y.idno) for y in student_list])
        elif (choice == 2):
            print("Add a book")
            book_title = raw_input("Book title: ")
            id_number = int(raw_input("Id number: "))
            cost = float(raw_input("Book price: "))

            book = Book(book_title, id_number, cost)
        
            ann.library.append(book)
            print ("Book added successfully")
            
        elif choice==3:
            print ("lending a book")
            idno=int(raw_input("enter sudent idno"))
            for x in student_list:
                if (x.idno == idno):
                    book_to_be_lent= raw_input("enter the book name")
                    for t in ann.library:
                        
                        if (t.title == book_to_be_lent):
                            date_borrowed= datetime.date.today()
                            date_returned =date_borrowed + datetime.timedelta(days =200)
                            loan = Loan(date_borrowed, date_returned)
                        
                            ann.books_lent.append({loan:t})
                            x.my_books.append(t)
                            ann.library.remove(t)
                            print("books lent %s" % [b.title for b in x.my_books])

        elif choice == 4:
            print ("Returning a book")
            idno = int(raw_input("Enter student id: "))
            book_borrowed_id = int(raw_input("Enter the id of the book you borrowed: "))

            for x in student_list:
                if (x.idno == idno):
                    for loan_book_dictionary in ann.books_lent:
                        #get the loan from dictionary { loan : book }
                        loan = loan_book_dictionary.keys()[0]
                        
                        # get book from dictionary
                        book = loan_book_dictionary.values()[0]
                        time_diff =abs((loan.date_returned - loan.date_borrowed).days) - 90

                        if (time_diff > 90):
                            fine = (time_diff/30.0)* 5000
                            print ("Fine is {}".format(fine))

                            x.fines.append(fine)                 
                        
                        if book.idno == book_borrowed_id:
                            ann.library.append(book)
                            # possible Error to check out

                            ann.books_lent.remove(loan_book_dictionary)
                            x.my_books.remove(book)
                            x.books_returned.append(book)
                            print ("books that were lent %s" % [b.values()[0].title for b in ann.books_lent])
                            print ("books in the library %s" % ann.library)
                            print ("books in the student's bag %s" % x.my_books)
                

            
        elif (choice == 5):
            
            for x in student_list:
                print ('Name of student:\t%s' %x.name)
                print ('\nBooks borrowed include')
                for y in x.my_books:
                    print '%s' %y.title

                print ('Total number of books borrowed:%d' %len(x.my_books))
                print ('The librarian is %s'%ann.name)
                print ('Number of books returned%s'%len(x.books_returned))
                
                print ('Total fine%d' %int(sum(x.fines)))
                    
                
        elif (choice == 7):
            break

                            


