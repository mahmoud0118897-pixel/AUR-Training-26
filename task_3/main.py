from library_system import Database, Library, Book, DVD, Magazine, Itemstatus

def main():

    db = Database("database.txt")
    library = Library(db)

    if not library.items:
        print("Adding initial items to the library...")
        try:

            book1 = Book(title="Dune", status=Itemstatus.AVAILABLE, author="Frank Herbert", isbn="9780441013593")
            library.add_item(book1)


            dvd1 = DVD(title="Inception", director="Christopher Nolan", status=Itemstatus.AVAILABLE)
            library.add_item(dvd1)

            mag1 = Magazine(title="National Geographic", issue="2026-08", status=Itemstatus.AVAILABLE)
            library.add_item(mag1)
            
            print("Items added successfully!\n")
        except ValueError as e:
            print(f"Error adding items: {e}")

    print("--- Available Items ---")
    for item in library.list_available():
        print(item)
    print("\n--- Checking out 'Dune' ---")
    try:
        library.checkout_item("Dune")
        print("Checkout successful!")
    except ValueError as e:
        print(f"Checkout Failed: {e}")


    print("\n--- Sorted Library Items ---")
    for item in library.get_sorted_items():
        print(item)

if __name__ == "__main__":
    main()