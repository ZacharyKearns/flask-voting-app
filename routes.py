from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/learningflask'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.secret_key = "development-key"

@app.route("/")
def index():
    return render_template("index.html.j2")

if __name__ == "__main__":
    app.run(debug=True)
