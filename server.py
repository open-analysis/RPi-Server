from flask import Flask, request, jsonify

app = Flask(__name__)

queue = []

@app.get("/queue")
def getQueue():
    global queue 
    json_queue = jsonify(queue)
    queue.clear()
    return json_queue

@app.post("/programs")
def add_program():
    if request.is_json:
        pass

@app.post("/devices")
def add_program():
    if request.is_json:
        pass