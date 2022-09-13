from select import select
import mysql.connector
myDb = mysql.connector.connect(host="localhost", user="root", passwd="123456",database="sql_clothing")
myCursor = myDb.Cursor()
selectCommand1 ="CREATE TABLE sql_customers (customerID int auto_increment primary key, fullName varchar(50) not null, address text, number int, prime int)"
selectCommand2 ="CREATE TABLE sql_store (store_ID int auto_increment primary key, name varchar(50) not null, address text, invID int, locId int)"
selectCommand3 ="CREATE TABLE sql_inventory (prodID int, name varchar(50) not null, description text, Qty int, price int, locID int)"
selectCommand4 ="CREATE TABLE sql_location (locId int, name varchar(50) not null)"
myCursor.execute(selectCommand1)
myCursor.execute(selectCommand2)
myCursor.execute(selectCommand3)
myCursor.execute(selectCommand4)
myDb.commit()
myDb.close()