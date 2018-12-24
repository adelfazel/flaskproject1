import os

from flask import Flask, session, render_template
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)
postgresURI = "postgres://bcvcpzwscndkyy:aec11e38db3ab3376ccadd2d83e3e308f60b542e633b44caea6ab7b1a4b422a4@ec2-54-235-169-191.compute-1.amazonaws.com:5432/d3n2ea3ie9begk"
postgresPASS = "aec11e38db3ab3376ccadd2d83e3e308f60b542e633b44caea6ab7b1a4b422a4"
postgresUSER = "bcvcpzwscndkyy"
postgresDB = "d3n2ea3ie9begk"
postgresPORT = 5432
# Check for environment variable
os.environ['DATABASE_URL'] = postgresURI
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    return "To DO"


@app.route("/register")
def register():
    return render_template("register.html")


if __name__ == '__main__':
    app.run(debug=True, port=5000)
