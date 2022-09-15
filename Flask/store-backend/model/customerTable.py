from db import db

class Customers(db.Model):
    __tablename__ = "sql_customers"
    customerId = db.Column(db.Integer, primary_key=True, nullable=False)
    fullName = db.Column(db.String(50), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    number = db.Column(db.String(10), nullable=False)
    prime = db.Column(db.Boolean, nullable=False)

    def convertRes(self):
        return {"id": self.customerId, "fullName": self.fullName, "address": self.address, "number": self.number}