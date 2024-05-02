from app.extensions import db

class Product(db.Model):
    
    __tablename__ = "product"
    name = db.Column(db.String(50), primary_key=True)
    price = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    
    
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description
        
        
    def get_full_product_name(self):
        return self.name

