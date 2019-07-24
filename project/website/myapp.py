from flask import Flask, render_template
import paho.mqtt.client as mqtt
from flask_socketio import SocketIO, emit

import concurrent.futures
#_____________1. init app_______________
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)
studentnumber = 0

#___________2.   Routers________________

#@app.rout('/help')
#def help():
#    return render_template('help.html') 

@app.route('/')
def index():
    print("here")
    global studentnumber
    print(studentnumber)
    return render_template('index.html',students = studentnumber )

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'studentnumber': message[studentnumber]})

@socketio.on('connect', namespace='/test')
def test_connect():
    emit('my response', {'studentnumber': studentnumber})

@socketio.on('disconnect', namespace='/test')
def test_disconnect():
    print('Client disconnected')
    
def on_connect(client,userdata,flag,rc): 
    print("Connected with result code"+str(rc))

    client.subscribe("#")

def on_message(client,userdata,msg):
    global studentnumber
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + "\n")
    studentnumber=msg.payload.decode("utf-8")
    test_message(studentnumber)


@app.route('/get_data', methods=['GET'])
def get_data():
    print("here")
    global studentnumber
    print(studentnumber)
    return jsonify(students = studentnumber)
    
def mqttloop(client):
    client.loop_forever()

#__________3.start server_____________________
if __name__== '__main__':
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("127.0.0.1",1883,60)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=3)
    executor.submit(mqttloop, client)
    print("blaa")
    socketio.run(app, debug=True, host='0.0.0.0',)
    
