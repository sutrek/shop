from extensions import db

class Products(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(50))
    remainder = db.Column(db.Integer, default=0)
    
    def __repr__(self):
        return f'<Product {self.name}>'

class Clients(db.Model):
    __tablename__ = 'clients'
    
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(200))
    order_history = db.Column(db.String(500))
    
    def __repr__(self):
        return f'<Client {self.login}>'
    