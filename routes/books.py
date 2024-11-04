from flask import Blueprint, jsonify, request
from m import fetch_books, add_book, delete_book

books_bp = Blueprint('books', __name__)

# Fetch all books
@books_bp.route('/books', methods=['GET'])
def get_books():
    books = fetch_books()
    return jsonify(books), 200

# Add a new book
@books_bp.route('/books', methods=['POST'])
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    price = data.get('price')
    description = data.get('description')
    stock = data.get('stock', 0)  # Set default stock to 0 if not provided
    
    # Make sure no required fields are None
    if not title or not author or not price or stock is None:
        return "Missing required fields", 400

    add_book(title, author, price, description, stock)
    return "Book added", 201

# Delete a book by ID
@books_bp.route('/books/<int:book_id>', methods=['DELETE'])
def remove_book(book_id):
    delete_book(book_id)
    return jsonify({"message": "Book deleted successfully!"}), 200
