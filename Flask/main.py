from flask import Flask
import constants
import socket
from flask_cors import CORS

app = Flask("Item Generator")


from controller import *
def start():
    print("rodou")
    cors = CORS(app)
    socket.setdefaulttimeout(100000)
    app.run(host='0.0.0.0', port=5000,debug=True)
if __name__ == '__main__':
    start()

