def main():
    try:
        #initialise books list
        BooksList =[]
        infile = open("TheBooksList.txt","r")
        line= infile.readline()
        while line:
            BooksList.append(line.rstrip("\n").split(","))
            line=infile.readline()
        infile.close()

    except FileNotFoundError:
        print("the <TheBooksList.txt> file is not found")
        print("Starting a new books list!")
        BooksList=[]

        

    choice = 0
    while choice != 5:
        print("*** Books Manager ***")
        print("1) Add a Book")
        print("2) Lookup a Book")
        print("3) Display Books")
        print("4) Delete a Book")
        print("5) Quit")
        choice=int(input())

        if choice==1:
            print("Adding a book...")
            nBook = input("Enter the name of book >>> ")

            nAuthor = input("Enter the author of book >>> ")

            nPage = input("Enter the pages of book >>> ")
            BooksList.append([nBook,nAuthor,nPage])

        elif choice == 2:
            print("Looking up for a book...")
            keyword = input("Enter Search Term: ").lower()

            found=False

            for book in BooksList:
                if keyword in book[0].lower() or keyword in book[1].lower():
                    print("Book Found: ",book) 
                    found=True

            if not found:
                print("No book found.")



        elif choice == 3:
            print("Displaying all books...")
            for i in range(len(BooksList)):
                 print(BooksList[i])

        elif choice == 4:
            print("Deleting a book...")
            book_name = input("Enter the name of the book to delete: ").strip().lower()

            found = False

            for book in BooksList:
                if book[0].strip().lower() == book_name:
                    BooksList.remove(book)
                    print("Book deleted successfully.")
                    found = True
                    break

            if not found:
                print("Book not found.")

        elif choice == 5:
            print("Quitting program")

        else:
            print("Invalid choice! Please select 1, 2, 3 or 4.")
    print("Program terminated")

    #Saving to external TXT file
    outfile = open("TheBooksList.txt","w")
    for book in BooksList:
        outfile.write(",".join(book) + "\n")
    outfile.close()




if __name__=="__main__":
    main()