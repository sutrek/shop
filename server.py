from flask import Flask, render_template, request, redirect, url_for
from flask_migrate import Migrate
from config import Config
from extensions import db
from models import Products, Clients

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

@app.route('/products/edit/<int:product_id>', methods=['GET', 'POST'])
def edit_product(product_id):
    product = Products.query.get_or_404(product_id)
    if request.method == 'POST':
        product.name = request.form['name']
        product.price = float(request.form['price'])
        product.category = request.form['category']
        product.remainder = int(request.form['remainder'])
        db.session.commit()
        return redirect(url_for('products'))
    return render_template('products_edit.html', product=product)

@app.route('/products/delete/<int:product_id>')
def delete_product(product_id):
    product = Products.query.get_or_404(product_id)
    db.session.delete(product)
    db.session.commit()
    return redirect(url_for('products'))


@app.route('/clients')
def clients():
    clients = Clients.query.all()
    return render_template('clients.html', clients=clients)

@app.route('/clients/add', methods=['GET', 'POST'])
def add_client():
    if request.method == 'POST':
        client = Clients(
            login=request.form['login'],
            address=request.form['address'],
            order_history=request.form['order_history']
        )
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('clients'))
    return render_template('clients_add.html', current_page="clients_add")

@app.route('/clients/edit/<int:client_id>', methods=['GET', 'POST'])
def edit_client(client_id):
    client = Clients.query.get_or_404(client_id)
    if request.method == 'POST':
        client.login = request.form['login']
        client.address = request.form['address']
        client.order_history = request.form['order_history']
        db.session.commit()
        return redirect(url_for('clients'))
    return render_template('clients_edit.html', client=client)

@app.route('/clients/delete/<int:client_id>')
def delete_client(client_id):
    client = Clients.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return redirect(url_for('clients'))

if __name__ == "__main__":
    app.run("0.0.0.0", port=5000, debug=True)
