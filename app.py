from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///laptops.db'

db = SQLAlchemy(app)


class Laptop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100))


@app.route('/')
def home():

    laptops = Laptop.query.all()

    text = ""

    for laptop in laptops:
        text += f"{laptop.model}<br>"

    return text


@app.route('/add/<model>')
def add(model):

    laptop = Laptop(model=model)

    db.session.add(laptop)
    db.session.commit()

    return "Laptop Added"


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(debug=True)
