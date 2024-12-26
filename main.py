from flask import Flask

from src import src
from routes.home import home_route
# from database import database

app = Flask(__name__)

app.register_blueprint(home_route)


if __name__ == '__main__':
    app.run(debug=True)
    # print(database.get_by_id(120))
    
    ...