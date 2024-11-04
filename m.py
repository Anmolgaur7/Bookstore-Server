from db_config import get_db_connection

def fetch_books():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    db.close()   
    return books

# Add a new book
def add_book(title, author, price, description, stock):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO books (title, author, price, description, stock) VALUES (%s, %s, %s, %s, %s)",
        (title, author, price, description, stock)
    )
    db.commit()
    db.close()

# Delete a book by its ID
def delete_book(book_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("DELETE FROM books WHERE id = %s", (book_id,))
    db.commit()
    db.close()

def add_user(name, email, password):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO users (name, email, password) VALUES (%s, %s, %s)", 
                   (name, email, password))
    db.commit()
    db.close()

def fetch_user(email, password):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE email = %s AND password = %s", (email, password))
    user = cursor.fetchone()
    db.close()
    return user

def add_to_cart(user_id, book_id, quantity):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO cart (user_id, book_id, quantity) VALUES (%s, %s, %s)", 
                   (user_id, book_id, quantity))
    db.commit()
    db.close()

def fetch_cart(user_id):
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM cart WHERE user_id = %s", (user_id,))
    cart_items = cursor.fetchall()
    db.close()
    return cart_items

def place_order(user_id):
    db = get_db_connection()
    cursor = db.cursor()
    cursor.execute("INSERT INTO orders (user_id) VALUES (%s)", 
                   (user_id))
    order_id = cursor.lastrowid
    db.commit()
    db.close()
    return order_id

# Function to remove an item from the cart
def remove_from_cart(user_id, item_id):
    try:
        db = get_db_connection()  
        cursor = db.cursor()
        cursor.execute("DELETE FROM cart WHERE user_id = %s AND id = %s", (user_id, item_id))
        if cursor.rowcount == 0:
            return {"error": "Item not found or already removed from the cart."}

        db.commit() 
        return {"message": "Item removed from cart successfully."}
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error removing item from cart: {e}")
        return {"error": "Failed to remove the item from the cart."}  
    finally:
        if db:
            db.close()

