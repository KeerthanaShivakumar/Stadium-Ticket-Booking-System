import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="")
c = mydb.cursor()

c.execute("create database if not exists stadiumTicket4")
c.execute("use stadiumTicket4")
