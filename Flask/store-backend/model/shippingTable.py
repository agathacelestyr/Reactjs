from db import db


class ShippingTable(db.Model):
    __tablename__ = "sql_shipping"
    ship_id = db.Column(db.Integer, primarykey=True, nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey(
        "sql_orders.order_id"), nullable=False)
    product_id = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(50), nullable=False)
    order = db.relationship("sql_orders")
    status = db.Column(db.String(1),)

    def __init__(self, order_id, product_id, location) -> None:
        super().__init__()
        self.order_id = order_id
        self.product_id = product_id
        self.location = location

    @classmethod
    def get_shippings_by_order_id(cls, orderId):
        cls.query.filter_by(order_id=orderId).all()

    def json(self):
        return {"id": self.ship_id, "orderId": self.order_id}