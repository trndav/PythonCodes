import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="bomb",
  password="somemysqlpassword"
)

print(mydb)