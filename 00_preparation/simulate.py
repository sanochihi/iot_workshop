#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a simple sensor data generator that sends to an MQTT broker via paho"""

import datetime
import random
import json
import paho.mqtt.client as mqtt

def get_data(i):
    """generate data and send it to an MQTT broker"""
    mqttc = mqtt.Client()

    mqttc.connect("localhost", 1883)

    interval_secs = 500 / 1000.0

    dt_now = datetime.datetime.now() + datetime.timedelta(hours=9)
    now_strftime = dt_now.strftime('%Y/%m/%d %H:%M:%S')

    data = {
        "lot_no": f"20221222-{i}",
        "date_time": now_strftime,
        "door_closed": 1,
        "hp_temperature": 72.8,
    }

    x = random.randint(1, 10)

    if x == 10:
        data["door_closed"] = 0

    if i == 1 and x == 1:
        y = data["hp_temperature"] + (random.randint(20, 30) / 10)
    else:
        y = data["hp_temperature"] + (x / 10)

    data["hp_temperature"] = round(y, 1)

    payload = json.dumps(data)
    print("%s" % payload)

    mqttc.publish("iot", payload)


for i in range(1, 4):
    get_data(i)