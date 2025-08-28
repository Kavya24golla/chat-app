# 🌈 Web Chat App

A **real-time web-based chat application** built with **Python, Flask, and Socket.IO**. Users can join the chat in their browser, send messages, and see messages from others instantly. Chat history is saved automatically.

## Features
- Real-time chat for multiple users in browser tabs or devices.
- Users can enter custom usernames.
- Chat history saved to `chat_log.txt`.
- Colorful and responsive UI with message bubbles.
- Fully browser-based—no terminal clients needed.
- ![Chat App Screenshot](image/app_.png)

## Project Structure
 #### chat-application/
├── client.py Flask + SocketIO server

├── chat_log.txt 

└── templates/

└── index.html 

## Installation
#### Clone the repository:

 bash

git clone https://github.com/kavya24golla/chat-app.git
cd chat-application
 ### Create a virtual environment:

python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows


 ### Install dependencies:

pip install flask flask-socketio eventlet

 ### How to Run

Start the server:

python client.py


### Open your browser and go to:

http://127.0.0.1:5000


Enter a username and start chatting!

Open multiple tabs or devices to chat with others in real-time.

