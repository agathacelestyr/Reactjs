from select import select
import mysql.connector
myDb = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="sql_clothing")
myCursor = myDb.cursor() 


class DbSync():
    @classmethod
    def create(cls, name, address, invID, locId):
        myDb = mysql.connector.connect(host="localhost", user="root", passwd="123456", database="sql_clothing")
        myCursor = myDb.cursor() 
        insertQuery = "INSERT INTO sql_store(name, address, invID, locId) VALUES (%s, %s, %s, %s)"
        val = [(name, address, invID, locId)]
        myCursor.executemany(insertQuery, val)
        myDb.commit()
 
class CustomersCont():
    @classmethod
    def create(cls, fullName, address, number, prime):
        insertQuery = "INSERT INTO sql_customers (fullName, address, number, prime) VALUES (%s, %s, %s, %s)"
        val =[(fullName, address, number, prime)]
        myCursor.executemany(insertQuery, val)
        myDb.commit()


class InventoryCont():
    @classmethod
    def create(cls, prodID, name, description, qty, price, locId):
        insertQuery = "INSERT INTO sql_inventory (prodID, name, description, qty, price, locId) VALUES (%s, %s, %s, %s)"
        val = [(prodID, name, description, qty, price, locId)]
        myCursor.executemany(insertQuery, val)
        myDb.commit()


class LocationCont():
    @classmethod
    def create(cls, locId, name):
        insertQuery = "INSERT INTO sql_location (locId, name) VALUES(%s, %s)"
        val = [(locId, name)]
        myCursor.executemany(insertQuery, val)
        myDb.commit()


        
        