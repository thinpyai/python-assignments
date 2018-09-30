from flask import Blueprint, render_template, request, url_for, flash
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('management', __name__)

@bp.route('/')
def index():
    db = get_db()
    books = db.execute(
        'SELECT * FROM book'
    ).fetchall()
    return render_template('book/bookList.html', books=books)



# @bp.route('/bookList', methods=('GET','POST'))
# @login_required
# def show_bookList():
#     books = get_db().execute(
#         'SELECT * FROM book WHERE p.id = ?',
#         (id,)
#     ).fetchall()
#     return render_template('book/bookList.html', books=books)

@bp.route('/addBook', methods=('GET','POST'))
@login_required
def addBook():
    if request.method == 'POST':
        name = request.form['name']
        writer = request.form['writer']
        type = request.form['type']
        db = get_db()
        error = None

        if not name:
            error = 'Book name is required.'

        elif not writer:
            error = 'Writer name is required.'

        if error is None:
            db.execute('INSERT INTO book (name, writer, type) VALUES (?, ?, ?)',
                       (name, writer,type))
            db.commit()
            return redirect(url_for('bookList'))
        flash(error)

    return render_template('book/addBook.html')

@bp.route('/detailBook', methods=('GET','POST'))
@login_required
def detailBook():
    return render_template('book/detailBook.html')

@bp.route('/borrowBook', methods=('GET','POST'))
@login_required
def borrowBook():
    return render_template('book/borrowBook.html')

@bp.route('/editBook', methods=('GET','POST'))
@login_required
def editBook():
    return render_template('book/editBook.html')

@bp.route('/deleteBook', methods=('GET','POST'))
@login_required
def deleteBook():
    return render_template('book/deleteBook.html')
