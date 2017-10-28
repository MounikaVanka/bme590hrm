from flask import Flask,request,jsonify
app= Flask(__name__)


@app.route("/hello/<:name>", methods=['GET'])
def hello(name):
    return "Hello " + name


@app.route("/data", methods=['GET'])
def getDict():
    temp = {"temp":[20,21,22]}
    time = {"time":[10,20,30]}
    arr = [temp, time]
    return jsonify(arr)


@app.route("/add", methods=['POST'])
def addEm():
    temp = {"temp":[20,21,22]}
    time = {"time":[10,20,30]}
    arr = [temp, time]
    return jsonify(arr)
