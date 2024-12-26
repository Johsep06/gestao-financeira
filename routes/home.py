from flask import Blueprint, render_template, jsonify
import datetime

home_route = Blueprint('home', __name__)

@home_route.route('/')
def home():
    return render_template('index.html')

@home_route.route('/year')
def get_year():
    today = datetime.date.today()
    return jsonify({'year':today.year})