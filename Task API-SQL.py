
''' Below questions executed after creating the data as below into the Mysql
Create Database ROUGH;
USE ROUGH;
create table family (`Name` varchar(50), `date` varchar(30))
select * from family;
insert into family values
('Sripad Kulkarni', '08-12-1992'),
('Sujata', '21-09-1993'),
('Appa', '01-04-1962'),
('Amma', '08-10-1969');
'''

# 1.	Write a program to insert a record in sql table via api

from flask import Flask,request, jsonify

app = Flask(__name__)
@app.route('/Q1',methods=['GET','POST'])
def Insert_SQL():
    a = "INSERT INTO ROUGH.FAMILY values("
    b = "'"
    c = ","
    d = ")"
    Name = request.json['num1']
    DOB = request.json['num2']
    s = a + b + Name + b + c + b + DOB + b + d
    if(request.method=='POST'):
        import mysql.connector as connection
        mydb = connection.connect(host="localhost", user="root", password="Abqp*1424")
        cursor = mydb.cursor() # This line will create the pointer
        cursor.execute ("use ROUGH") # To set MySql to use the selected database
        cursor.execute(s)
        mydb.commit()
        cursor.close()
        return jsonify("completed")

# 2.	Write a program to update a record via api in sql

@app.route('/Q2',methods=['GET','POST'])
def Update_SQL():
    a = "update family set `date` = "
    b = "'"
    c = "where `Name` ="
    Name = request.json['num1']
    DOB = request.json['num2']
    s = a + b + DOB + b + c + b + Name + b
    if(request.method=='POST'):
        import mysql.connector as connection
        mydb = connection.connect(host="localhost", user="root", password="Abqp*1424")
        cursor = mydb.cursor() # This line will create the pointer
        cursor.execute ("use ROUGH") # To set MySql to use the selected database
        cursor.execute(s)
        mydb.commit()
        cursor.close()
        return jsonify("completed")

# 3.	Write a program to delete a record via api in sql

@app.route('/Q3',methods=['GET','POST'])
def Drop_Record_SQL():
    a = "Delete from family where `Name` = "
    b = "'"
    Name = request.json['num1']
    s = a + b + Name + b
    if(request.method=='POST'):
        import mysql.connector as connection
        mydb = connection.connect(host="localhost", user="root", password="Abqp*1424")
        cursor = mydb.cursor() # This line will create the pointer
        cursor.execute ("use ROUGH") # To set MySql to use the selected database
        cursor.execute(s)
        mydb.commit()
        cursor.close()
        return jsonify("completed")

# 4.	Write a program to fetch a record via api in sql

@app.route('/Q4',methods=['GET','POST'])
def Fetch_Record_SQL():
    if(request.method=='POST'):
        a = "select * from "
        Table_Name = request.json['num1']
        b = a+Table_Name
        import mysql.connector as connection
        mydb = connection.connect(host="localhost", user="root", password="Abqp*1424")
        cursor = mydb.cursor() # This line will create the pointer
        cursor.execute ("use ROUGH") # To set MySql to use the selected database
        cursor.execute(b)
        l = []
        for i in cursor.fetchall():
            l.append(i)
        return jsonify(l)
        mydb.commit()
        cursor.close()

if __name__=='__main__':
    app.run()

