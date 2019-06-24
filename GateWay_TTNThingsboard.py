# -*- coding: utf-8 -*-
"""
Théo Guiguitant 
theo.guiguitant@gmail.com

script that from an MQTT client (subscribe to TTN) 
makes http requests to the Things Boards system API
"""

import paho.mqtt.client as mqtt_client
from Lib import *

printlog("Script Gateway TTN to Thingsboard has begin")


dPrm = getIniParameters("commissioning.ini") #loading of all keys and connection parameters


client = mqtt_client.Client( client_id=dPrm['MQTT']['clientid'] ) #launch of the mqtt client
printlog("Client MQTT begin ")

#interrupt function
client.on_message = on_message
client.on_connect = on_connect
#client.on_log = on_log 
# Connexion broker

client.username_pw_set(username=dPrm['TTN']['appid'], password=dPrm['TTN']['accesskey'] )
client.connect(host=dPrm['MQTT']['broker'], port=int(dPrm['MQTT']['port']), keepalive=int(dPrm['MQTT']['keep_alive']))
printlog("Client MQTT connect to TTN")
client.subscribe( "+/devices/+/up" )

# standby loop
client.loop_forever()
