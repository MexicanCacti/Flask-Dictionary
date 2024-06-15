import functools

from flask import(
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from dict.db import get_db

bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/test',methods=('GET','POST'))
def home():
    return render_template('home/home.html')