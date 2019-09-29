import urllib.request
import json
import time
import numpy as np
import pandas as pd


def get_meter_json(url, username, password):
    # Prepare for http basic auth
    auth_handler = urllib.request.HTTPBasicAuthHandler()
    auth_handler.add_password(realm="Provide password for API service", uri=url, user=username, passwd=password)
    opener = urllib.request.build_opener(auth_handler)

    # Fetch data
    with opener.open(url) as req:
        data = req.read().decode("utf-8")

    # Decode JSON
    return json.loads(data)


def map_obis(values):
    obis_map = {
        "1-0:1.8.0*255"  : "consumption_total",
        "1-0:2.8.0*255"  : "production_total",
        "1-0:21.7.0*255" : "power_phase1",
        "1-0:41.7.0*255" : "power_phase2",
        "1-0:61.7.0*255" : "power_phase3",
        "1-0:36.7.0*255" : "power_phase1",
        "1-0:56.7.0*255" : "power_phase2",
        "1-0:76.7.0*255" : "power_phase3",
        "1-0:32.7.0*255" : "voltage_phase1",
        "1-0:52.7.0*255" : "voltage_phase2",
        "1-0:72.7.0*255" : "voltage_phase3",
        "1-0:1.7.0*255"  : "power_total",
    }

    result = {}
    for value in values:
        if value["type"] != "OBIS":
            continue

        obis = value["obis"]
        try:
            semantic = obis_map[obis]

            # The meter readings are stored as integer with a scaler
            # to keep the maximum accurancy. For easier handling we
            # convert it into a float and willingly loose some
            # precision.
            result[semantic] = {
                "value" : value["value"] * pow(10, value["scaler"]),
                "unit" : value["unit_text"],
            }

        except KeyError:
            continue

    return result


if __name__ == '__main__':
  url = "http://192.168.128.1:8080/api/meter"
  username = "api"
  password = "hackathon"
  key = '1ESY1161230623'
  old_timestamp = ''
  dict = {}

  device_name = input('Geraetename:')

  values = []
  last_energy = -1.0

  while True:
      try:
          data = get_meter_json(url, username, password)
          timestamp = data[key]['received']
          if timestamp == old_timestamp:
              time.sleep(0.3)
          else:
              measurement = data[key]['measurements'][0]
              # Live measurement?
              if measurement["storage"] != 0:
                  print('DATA NOT LIVE')

              mapped_values = map_obis(measurement["values"])
              if len(mapped_values) > 0:
                  result = mapped_values
                  dict[timestamp] = result['power_phase3']
              old_timestamp = data[key]['received']

              if last_energy == -1.0:
                  last_energy = result['consumption_total']['value']

              values.append((timestamp, result['power_phase3']['value'], result['consumption_total']['value'] - last_energy))
              last_energy = result['consumption_total']['value']

              if len(values) > 9:
                  # send values to serve

                  myurl = "http://127.0.0.1:5000/Test"
                  req = urllib.request.Request(myurl)
                  req.add_header('Content-Type', 'application/json; charset=utf-8')
                  jsondata = json.dumps(values)
                  jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
                  req.add_header('Content-Length', len(jsondataasbytes))
                  response = urllib.request.urlopen(req, jsondataasbytes)
                  values.pop(0)
              print(values[-1])
      except KeyboardInterrupt:
          df = pd.DataFrame.from_dict(dict, orient = "index").reset_index()
          df.to_csv('./' + device_name + '.csv', index=False)
          break
