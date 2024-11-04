from flask import Flask
from flask_cors import CORS
from routes.books import books_bp
from routes.users import users_bp
from routes.cart import cart_bp

app = Flask(__name__)
CORS(app,origins=["http://localhost:3000"])

# Register blueprints
app.register_blueprint(books_bp)
app.register_blueprint(users_bp)
app.register_blueprint(cart_bp)

@app.route('/')
def home():
    return "Welcome to the Bookstore API"

if __name__ == '__main__':
    app.run(debug=True)
