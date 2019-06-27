# -*- coding: utf-8 -*-
"""
Théo Guiguitant 
theo.guiguitant@gmail.com

script that from an MQTT client (subscribe to TTN) 
makes http requests to the Things Boards system API
"""

import paho.mqtt.client as mqtt_client
from lib import *

printlog("Script Gateway TTN to Thingsboard has begin")


dPrm = getIniParameters("commissioning.ini") #loading of all keys and connection parameters
for key, value in dPrm.items():
    for key2,value in dPrm[key].items():
            if value=="":
                sys.exit("Error message: commissioning incomplete")

client = mqtt_client.Client( client_id=dPrm['MQTT']['clientid'] ) #launch of the mqtt client

printlog("1/3 - Client MQTT begin ")

#interrupt function
client.on_message = on_message
client.on_connect = on_connect
#client.on_log = on_log 
# Connexion broker

client.username_pw_set(username=dPrm['TTN']['appid'], password=dPrm['TTN']['accesskey'] )
while True:
    try:
        printlog("2/3 - connect in progress...")
        client.connect(host=dPrm['MQTT']['broker'], port=int(dPrm['MQTT']['port']), keepalive=int(dPrm['MQTT']['keep_alive']))
        break
    except TimeoutError as e:
        printlog("Timeout: (Probably: not route with the broker)")
        printlog(str(e))
        continue
    except OSError as e:
        printlog("OSError: (Probably: not permission to open port Mqtt)")
        printlog(str(e))
        continue
    

client.subscribe(dPrm['MQTT']['topic'])
printlog("3/3 - Client MQTT is connected with TTN broker")
# standby loop
client.loop_forever()
