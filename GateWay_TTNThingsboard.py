# -*- coding: utf-8 -*-
"""
Théo Guiguitant 
theo.guiguitant@gmail.com
"""
import paho.mqtt.client as mqtt_client
from Lib import *

printlog("lancement du script Gateway TTN vers Thingsboard")
dPrm = getIniParameters("commissioning.ini")
client = mqtt_client.Client( client_id=dPrm['MQTT']['clientid'] )
printlog("Client MQTT begin ")
# Assignation des fonctions de rappel
client.on_message = on_message
client.on_connect = on_connect
#client.on_log = on_log 
# Connexion broker
client.username_pw_set(username=dPrm['TTN']['appid'], password=dPrm['TTN']['accesskey'] )
client.connect(host=dPrm['MQTT']['broker'], port=int(dPrm['MQTT']['port']), keepalive=int(dPrm['MQTT']['keep_alive']))
printlog("Client MQTT connect to TTN")
client.subscribe( "+/devices/+/up" )

# Envoi des messages
client.loop_forever()
