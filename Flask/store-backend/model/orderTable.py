from db import db


class OrdersTable(db.Model):
    __tablename__ = "sql_orders"
    order_id = db.Column(db.Integer, primarykey=True, nullable=False)
    shipping_id = db.Column(db.Integer, nullable=False)
    products = db.Column(db.Text, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)

    def __init__(self, shipping, products, custId) -> None:
        super().__init__()
        self.shipping_id = shipping
        self.products = products
        self.customer_id = custId