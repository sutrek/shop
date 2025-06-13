from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from config import Config
from extensions import db
from models import Products

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return render_template("index.html", current_page="main")

@app.route('/products')
def products():
    products = Products.query.all()
    return render_template('products.html', products=products)

@app.route('/products/add', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        product = Products(
            name=request.form['name'],
            price=float(request.form['price']),
            category=request.form['category'],
            remainder=int(request.form['remainder'])
        )
        db.session.add(product)
        db.session.commit()
        return redirect(url_for('products'))  


    return render_template('products_add.html', current_page="products_add")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)