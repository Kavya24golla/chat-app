from flask import Flask, render_template, request
from flask_socketio import SocketIO, send
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)


if not os.path.exists("chat_log.txt"):
    open("chat_log.txt", "w").close()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
    print(msg)
    send(msg, broadcast=True)
    
    with open("chat_log.txt", "a", encoding="utf-8") as f:
        f.write(msg + "\n")

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000, allow_unsafe_werkzeug=True)
