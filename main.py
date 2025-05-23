from flask import Flask

from database import database
from routes.home import home_route
from routes.forms import forms_route
from routes.data import data_route

app = Flask(__name__)

database.init_db()
app.register_blueprint(home_route)
app.register_blueprint(forms_route, url_prefix='/forms')
app.register_blueprint(data_route, url_prefix='/data')

if __name__ == '__main__':
    app.run(debug=True)