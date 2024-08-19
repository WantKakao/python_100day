from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

'''
On Windows type:
python -m pip install -r requirements.txt
'''

app = Flask(__name__)

# CREATE DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///new-books-collection.db"
# Optional: But it will silence the deprecation warning in the console.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CREATE TABLE
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    # Optional: this will allow each book object to be identified by its title when printed.
    def __repr__(self):
        return f'<Book {self.title}>'
#
#
# with app.app_context():
#     db.create_all()

#     new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
#     db.session.add(new_book)
#     db.session.commit()

# ---------------------------------- SQLite CRUD --------------------------------------
# 새 레코드 만들기
# new_book = Book(id=1, title="Harry Potter", author="J. K. Rowling", rating=9.3)
# db.session.add(new_book)
# db.session.commit()

# 모든 레코드 읽기
# all_books = session.query(Book).all()

# flask-sqlalchemy 로 읽는 법
# books = Book.query.all()

# 쿼리별 특정 레코드 읽기
# book = Book.query.filter_by(title="Harry Potter").first()

# 쿼리별 레코드 업데이트하기
# book_to_update = Book.query.filter_by(title="Harry Potter").first()
# book_to_update.title = "Harry Potter and the Chamber of Secrets"
# db.session.commit()

# 기본키로 레코드 업데이트하기
# book_id = 1
# book_to_update = Book.query.get(book_id)
# book_to_update.title = "Harry Potter and the Goblet of Fire"
# db.session.commit()

# 기본키로 특정 레코드 삭제하기
# book_id = 1
# book_to_delete = Book.query.get(book_id)
# db.session.delete(book_to_delete)
# db.session.commit()
# -------------------------------------------------------------------------------------


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        new_book = {
            'title': request.form['name'],
            'author': request.form['author'],
            'rating': request.form['rate']
        }
        all_books = Book.query.all()
        all_books.append(new_book)
        with app.app_context():
            book = Book(title=new_book['title'], author=new_book['author'], rating=new_book['rating'])
            db.session.add(book)
            db.session.commit()

        return redirect(url_for('home'))

    return render_template('add.html')


@app.route('/edit', methods=['GET', 'POST'])
def edit():
    book_id = request.args.get('id', type=int)  # URL 쿼리 파라미터에서 책 ID 가져오기
    book = Book.query.get(book_id)

    if request.method == 'POST':
        new_rating = request.form.get('rate')
        book.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('edit.html', book=book)


@app.route('/delete')
def delete():
    book_id = request.args.get('id', type=int)
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)
