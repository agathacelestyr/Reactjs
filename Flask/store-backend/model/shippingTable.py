from db import db


class ShippingTable(db.Model):
    __tablename__ = "sql_shipping"
    ship_id = db.Column(db.Integer, primarykey=True, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey(
        "sql_orders.order_id"), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    order = db.relationship("sql_orders")

    def __init__(self, order_id, product_id, location) -> None:
        super().__init__()
        self.order_id = order_id
        self.product_id = product_id
        self.location = location