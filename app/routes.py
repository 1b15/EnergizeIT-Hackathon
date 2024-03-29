from flask import render_template
from flask import request
from app import app
from app import socketio
import json
from app import classifier
from flask_socketio import send, emit
from app import loaded_model

stat_data = {
  "probabilities": [],
  "lastTen": [],
  "totalConsumption": [0,0,0]
}
@app.route('/',methods=['GET'])
def hello_world():
  return render_template('index.html')

# WHEN A SOCKET CONNECTS: Answer messages to server via Websocket.
# We probably dont want a while loop for every user on the actual server.
# Should send newest Data-set ( Top n), to fix missed messages.
# Only store sum of usage? Storing last 100 seconds would be quite expensive with sufficient clients.

@app.route('/Test',methods=['POST'])
def model_data():
  data = request.get_json()
  print(data)
  result = []

  for arr in data:
    result.append(arr[1])

  print(result)
  stat_data['lastTen'] = result
  classifierRes = classifier.classify_device(loaded_model, result[-4:])
  consumptionIndex = classifierRes.index(max(classifierRes))

  if consumptionIndex > 2:
    consumptionIndex = 2
  print(consumptionIndex)
  print(data[9])
  stat_data['totalConsumption'][consumptionIndex] += data[9][2]
  stat_data['probabilities'] = classifierRes
  return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}


@socketio.on('giveData')
def handle_message():
    print("Send Data ")
    socketio.emit('giveData',json.dumps(stat_data))