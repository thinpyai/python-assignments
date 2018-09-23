from flask import Blueprint, render_template, request, url_for
from werkzeug.exceptions import abort
from werkzeug.utils import redirect

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('management', __name__)

@bp.route('/')
def index():
    return redirect(url_for('auth.login'))

@bp.route('/bookList', methods=('GET','POST'))
@login_required
def show_bookList():
    books = get_db().execute(
        'SELECT * FROM book WHERE p.id = ?',
        (id,)
    ).fetchall()

    return render_template('blog/index.html', books=books)
