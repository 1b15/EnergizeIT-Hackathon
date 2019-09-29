from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

from keras.models import load_model
loaded_model = load_model('model.h5')

from app import routes