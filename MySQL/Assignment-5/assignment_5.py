# Using Python MySQL connector to perform CRUD operations
import mysql.connector

# Creating database object
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'vishwak@05',
    database = 'customer_db'
)

# Creating cursor object
cursorObj = database.cursor()

# Method to create Table books
def create_table():
    create_query = """
        CREATE TABLE IF NOT EXISTS books (
            id INT PRIMARY KEY AUTO_INCREMENT,
            title VARCHAR(50) NOT NULL,
            author VARCHAR(50) NOT NULL,
            genre VARCHAR(50) NOT NULL,
            publication_year YEAR NOT NULL,
            language VARCHAR(20),
            price DECIMAL(10,2),
            isbn VARCHAR(20) NOT NULL,
            publisher VARCHAR(50),
            rating FLOAT
        )
    """
    cursorObj.execute(create_query)
    database.commit()

# Method to insert data into books
def insert_data(book):
    insert_query = """
        INSERT INTO books (title, author, genre, publication_year, language, price, isbn, publisher, rating) VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s, %s);
    """
    data_tuple = (
        book['title'], book['author'], book['genre'], book['publication_year'], 
        book['language'], book['price'], book['isbn'], book['publisher'], book['rating']
    )
    cursorObj.execute(insert_query, data_tuple)
    database.commit()

# Method to read data in books
def read_data():
    read_query = "SELECT * FROM books;"
    cursorObj.execute(read_query)
    result = cursorObj.fetchall()
    return result

# Method to update data in books
def update_data(book_id, book):
    fields = ', '.join(f"{k}=%s" for k in book.keys())
    values = list(book.values())
    values.append(book_id)
    update_query = f"UPDATE books SET {fields} WHERE id = %s;"
    cursorObj.execute(update_query, values)
    database.commit()

# Method to delete data in books
def delete_data(book_id):
    delete_query = "DELETE FROM books WHERE id = %s"
    cursorObj.execute(delete_query, (book_id,))
    database.commit()

if __name__ == "__main__":
    print("Creating the Table books in Database:")
    create_table()
    print("Successfully created Table books")

    print("\nInserting Data into Table books:")
    book1 = {
        'title':'The Great Gatsby',
        'author': 'F. Scott Fitzgerald',
        'genre': 'Classic',
        'publication_year': 1925,
        'language': 'English',
        'price': 399.99,
        'isbn': '9780743273565',
        'publisher': 'Scribner',
        'rating': 4.5
    }
    insert_data(book=book1)

    book2 = {
        'title':'To Kill a Mockingbird',
        'author': 'Harper Lee',
        'genre': 'Classic',
        'publication_year': 1960,
        'language': 'English',
        'price': 299.50,
        'isbn': '9780061120084',
        'publisher': 'J.B. Lippincott & Co.',
        'rating': 4.8
    }
    insert_data(book=book2)

    book3 = {
        'title':'One Hundred Years of Solitude',
        'author': 'Gabriel Garcia Marquez',
        'genre': 'Magical Realism',
        'publication_year': 1967,
        'language': 'Spanish',
        'price': 499.00,
        'isbn': '9780060883287',
        'publisher': 'Harper & Row',
        'rating': 4.7
    }
    insert_data(book=book3)

    book4 = {
        'title':'Sapiens',
        'author': 'Yuval Noah Harari',
        'genre': 'Non-fiction',
        'publication_year': 2011,
        'language': 'English',
        'price': 550.00,
        'isbn': '9780099590088',
        'publisher': 'Harvill Secker',
        'rating': 4.6
    }
    insert_data(book=book4)
    print("Inserted all Data into Table books successfully")

    print("\nReading the Data in Table books:")
    data = read_data()
    print("id, title, author, genre, publication_year, language, price, isbn, publisher, rating")
    for id, title, author, genre, publication_year, language, price, isbn, publisher, rating in data:
        print(f"{id}, {title}, {author}, {genre}, {publication_year}, {language}, {price}, {isbn}, {publisher}, {rating}")
    
    print("\nUpdating Data in Table books:")
    update_book2 = {
        'price': 349.50,
        'rating': 4.7
    }
    update_data(book_id=2, book=update_book2)
    print("Data in book_id:2 updated successfully")

    print("\nDeleting Data in Table books:")
    delete_data(book_id=4)
    print("Deleted Data of book_id:4 successfully\n")

    data = read_data()
    print("id, title, author, genre, publication_year, language, price, isbn, publisher, rating")
    for id, title, author, genre, publication_year, language, price, isbn, publisher, rating in data:
        print(f"{id}, {title}, {author}, {genre}, {publication_year}, {language}, {price}, {isbn}, {publisher}, {rating}")
    
    cursorObj.close()
    database.close()
