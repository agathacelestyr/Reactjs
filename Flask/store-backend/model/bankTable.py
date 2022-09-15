from db import db


class BankTable(db.Model):
    __tablename__ = "sql_bank"
    order_id = db.Column(db.Integer, db.ForeignKey(
        "sql_orders.order_id"), primarykey=True, nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    currency = db.Column(db.String(50), nullable=False)
    order = db.relationship("sql_orders")

    def __init__(self, order_id, amount, currency) -> None:
        super().__init__()
        self.order_id = order_id
        self.amount = amount
        self.currency = currency