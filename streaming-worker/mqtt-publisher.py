import time
from datetime import datetime
import json
import random

import paho.mqtt.client as mqtt

broker = 'mqtt.eclipseprojects.io'
port = 1883
topic = 'mqtt_topic'

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code):
    print(f"Connected with result code {reason_code}")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

def simulate_data(msg_count):
    factor = random.random()
    msg = '{ "time":"' + str(datetime.now()) + '", "P_Bus1":"' + str(msg_count * factor) + '", "Q_Bus1":"' + str(msg_count / factor) + '"}'
    return msg

def publish(client):
    msg_count = 1
    while True:
        time.sleep(1)
        msg = simulate_data(msg_count)
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1
        #if msg_count > 5:
        #    break

mqttc = mqtt.Client()
mqttc.on_connect = on_connect

mqttc.connect("mqtt.eclipseprojects.io", 1883, 60)

mqttc.loop_start()
publish(mqttc)
mqttc.loop_stop()