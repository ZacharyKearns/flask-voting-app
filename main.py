from flask import Flask
from models import db
from routes import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://psciupthjhnfbi:d18c73a8cc96fc3733507a5144a94c8fe4747ae77b0584541046d32b3d705e8c@ec2-184-73-236-170.compute-1.amazonaws.com:5432/dcj3a6sju72t1i'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# protect against CSRF
app.secret_key = "development-key"

# register routes
app.register_blueprint(routes)

if __name__ == "__main__":
    app.run(debug = True)
