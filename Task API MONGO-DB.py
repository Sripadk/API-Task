#1.	Write a program to insert a record in sql table via api
#2.	Write a program to update a record via api
#3.	Write a program to delete a record via api
#4.	Write a program to fetch a record via api
# 5.	All the above questions you have to answer for mongo db as well.
# First We insert data into MongoDB
# First we insert some data into MongoDB and mark it down to prevent iteration.
'''
import pymongo

data = [
    {"Name" :"Sripad", "DOB" : "08-12-1992"},
{"Name" :"Sujata", "DOB" : "21-09-1993"},
{"Name" :"Appa", "DOB" : "01-04-1962"},
{"Name" :"Amma", "DOB" : "05-10-1967"}
]

client = pymongo.MongoClient("mongodb+srv://SRIPAD:sripad@cluster0.wqd95wk.mongodb.net/?retryWrites=true&w=majority")
db = client.test

# print(db)

db1 = client["API_Task"]
coll = db1["family"]
coll.insert_many(data)
# After inserting the above data the above code was marked down
# Q1.	Write a program to insert a record in MongoDB via api
'''
from flask import Flask, request, jsonify

app = Flask(__name__)

# Q1.	Write a program to insert a record in MongoDB via api

@app.route('/Q1',methods=['GET','POST'])
def Insert_MongoDB():
    if (request.method == 'POST'):
        Name = request.json['num1']
        DOB = request.json['num2']
        import pymongo
        client = pymongo.MongoClient(
            "mongodb+srv://SRIPAD:sripad@cluster0.wqd95wk.mongodb.net/?retryWrites=true&w=majority")
        db1 = client["API_Task"]
        coll = db1["family"]
        l = [{'Name':Name,'DOB':DOB}]
        coll.insert_many(l)
        return jsonify("completed record insertion")

#2.	Write a program to update a record via api

@app.route('/Q2',methods=['GET','POST'])
def Update_Record_MongoDB():
    if (request.method == 'POST'):
        Name = request.json['num1']
        Update = request.json['num2']
        import pymongo
        client = pymongo.MongoClient(
            "mongodb+srv://SRIPAD:sripad@cluster0.wqd95wk.mongodb.net/?retryWrites=true&w=majority")
        db1 = client["API_Task"]
        coll = db1["family"]
        coll.update_one({'Name': Name}, {'$set': {'Name': Update}})
        return jsonify("completed record insertion")

#3.	Write a program to delete a record via api

@app.route('/Q3',methods=['GET','POST'])
def Delete_Record_MongoDB():
    if (request.method == 'POST'):
        Name = request.json['num1']
        import pymongo
        client = pymongo.MongoClient(
            "mongodb+srv://SRIPAD:sripad@cluster0.wqd95wk.mongodb.net/?retryWrites=true&w=majority")
        db1 = client["API_Task"]
        coll = db1["family"]
        coll.delete_one({'Name': Name})
        return jsonify("completed record insertion")

#4.	Write a program to fetch a record via api

@app.route('/Q4',methods=['GET','POST'])
def Fetch_Record_MongoDB():
    if (request.method == 'POST'):
        Name = request.json['num1']
        import pymongo
        from bson.json_util import dumps
        client = pymongo.MongoClient(
            "mongodb+srv://SRIPAD:sripad@cluster0.wqd95wk.mongodb.net/?retryWrites=true&w=majority")
        db1 = client["API_Task"]
        coll = db1["family"]
        record = coll.find({'Name': Name})
        l = list(record)
        json_data = dumps(l)
        return jsonify(json_data)


if __name__ == "__main__":
    app.run()