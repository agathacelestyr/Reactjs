from db import db


class OrdersTable(db.Model):
    __tablename__ = "sql_orders"
    order_id = db.Column(db.Integer, primarykey=True,
                         nullable=False, backref="sql_orders")
    shipping_id = db.Column(db.Integer, nullable=False)
    products = db.Column(db.Text, nullable=False)
    customer_id = db.Column(db.Integer, nullable=False)
    shippings = db.realtionship("sql_shipping")

    def __init__(self, shipping, products, custId) -> None:
        super().__init__()
        self.shipping_id = shipping
        self.products = products
        self.customer_id = custId

    def add_order(self):
        db.session.add(self)
        db.session.commit()

    def json(self):
        return {"id": self.order_id, "shippingId": self.shipping_id, "shippings": [ship.json() for ship in self.shippings.all()]}

    @classmethod
    def get_order_by_id(cls, order_id):
        return cls.query.filter_by(order_id=order_id).first()