from flask import Flask
from models import db
from routes import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/votingapp'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# protect against CSRF
app.secret_key = "development-key"

# register routes
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug = True)
