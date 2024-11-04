from flask import Blueprint, request, jsonify
from m import add_to_cart, fetch_cart, place_order,remove_from_cart

cart_bp = Blueprint('cart', __name__)

@cart_bp.route('/cart', methods=['POST'])
def add_cart_item():
    data = request.get_json()
    print(data)
    user_id = data.get('user_id')
    book_id = data.get('book_id')
    quantity = data.get('quantity')

    add_to_cart(user_id, book_id, quantity)
    return jsonify({"message": "Item added to cart!"}), 200

@cart_bp.route('/cart/<int:user_id>', methods=['GET'])
def get_cart_items(user_id):
    cart_items = fetch_cart(user_id)
    return jsonify(cart_items), 200

@cart_bp.route('/order', methods=['POST'])
def create_order():
    data = request.get_json()
    print(data)
    user_id = data.get('user_id')

    order_id = place_order(user_id)
    return jsonify({"message": "Order placed successfully!", "order_id": order_id}), 201

@cart_bp.route('/cart/<int:user_id>/item/<int:item_id>', methods=['DELETE'])
def remove_cart_item(user_id, item_id):
    try:
        print(user_id)
        print(item_id)
        remove_from_cart(user_id, item_id)  # Implement this function in your model
        return jsonify({"message": "Item removed from cart!"}), 200
    except Exception as e:
        print("Error removing item from cart:", e)  # Log the error for debugging
        return jsonify({"error": "Failed to remove item from cart."}), 500
