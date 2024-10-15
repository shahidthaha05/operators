import mysql.connector

con=mysql.connector.connect(user='shahid',host='localhost',password='shahidthaha@2005',database='batch2')
con.autocommit=True
cur=con.cursor()
# cur.execute("create database batch2")


# cur.execute("create table std (roll int,name text,age int)")

try:
    cur.execute("create table std (roll int,name text,age int)")
except:
    pass

rollno=int(input("enter roll no : "))
name=input("enter the name : ")
age=int(input("enter the age : "))

cur.execute("insert into std (roll ,name ,age ) values(%s,%s,%s)",(rollno,name,age))
con.commit()