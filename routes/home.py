from flask import Blueprint, render_template
import datetime

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')

@home_route.route('/year')
def year():
    today = datetime.date.today()

    return render_template('year.html', year=today.year)