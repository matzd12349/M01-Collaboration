from flask import Flask, request
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'

db = SQLAlchemy(app)
app.app_context().push() 

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80))
    publisher = db.Column(db.String(80))

    def __repr__(self):
        return(f"{self.id} - {self.name} - {self.author} - {self.publisher}")

@app.route('/')
def index():
    return('hello')

@app.route('/books')
def get_books():
    books = Book.query.all()

    output = []
    for book in books:
        book_info = {'id':book.id, 'name': book.name, 'author':book.author, 'publisher':book.publisher}
        output.append(drink_data)
    return {"books": output}

@app.route('/books/<id>')
def get_books(id):
    book = Book.query.get_or_404(id)
    return {'id':book.id, 'name': book.name, 'author':book.author, 'publisher':book.publisher}

@app.route('/books', methods=['POST'])
def add_book():
    book = Book(id=request.json['id'], name=request.json['name'], author=request.json['author'], publisher=request.json['publisher'])
    db.session.add(book)
    db.session.commit()
    return {'id':book.id}

@app.route('/books', methods=['DELETE'])
def delete_drink(id):
    book = Books.query.get(id)
    if drink is None:
        return {"error": "not found"}
    db.session.delte(book)
    db.session.commit()
    return {"message":"all good"}