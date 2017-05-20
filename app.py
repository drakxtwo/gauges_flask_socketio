#!/usr/bin/env python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from random import randint
async_mode = None

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, async_mode=async_mode)
thread = None

def background_thread():
    """Example of how to send server generated events to clients."""
    ext=fr=kt=bd=elec=0
    while True:
        socketio.sleep(2)
        ext = randint(-10,30)
        fr = randint(10,30)
        kt = randint(10,30)
        bd = randint(10,30)
        elec = randint(0,8000)
        
        socketio.emit('my_response',
                      {'data':'Values', 'elec': elec,'ext': ext,'fr': fr,'kt': kt,'bd': bd},
                      namespace='/carpi')


mesg = 'we are here...'
@app.route('/')
def index():
    speed = randint(0,133)
    templateData={
        'mesg' :mesg,
        'speed' :speed
    }
    return render_template('index.html', async_mode=socketio.async_mode, **templateData)

@socketio.on('connect', namespace='/carpi')
def test_connect():
    global thread
    if thread is None:
        thread = socketio.start_background_task(target=background_thread)

if __name__ == '__main__':
    socketio.run(app, debug=True)
