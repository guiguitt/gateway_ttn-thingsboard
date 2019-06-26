# GateWay_TTNThingsboard
This script allows you to receive messages published on MQTT topic, 
select data, and publish this data via HTTP request.
the script is developed to work between The Things Network and Things Board. 
The ThingsBoard Professional Edition  of Things Board allows you to read a Topic MQTT directly and a Gateway module 
is available to do the same.
### other ways of doing things 
* [Professional Edition-MQTT](https://thingsboard.io/docs/user-guide/integrations/mqtt/) 
* [Module gateway iot](https://thingsboard.io/docs/iot-gateway/)
## Getting Started
* download the zip of the project
```
https://github.com/guiguitt/GateWay_TTNThingsboard/archive/master.zip
```
* or clone on your computer 
```
https://github.com/guiguitt/GateWay_TTNThingsboard.git
```
### Python
to execute the script that requires the python environment.
for linux:
```
https://docs.python-guide.org/starting/install3/linux/
```
for windows: 
```
http://winpython.sourceforge.net/
```
and 4 module
* Paho-mqtt
```
pip install paho-mqtt
```
* requests
```
pip install requests
````
* json
* datatime
### Commissioning
MQTT
1. BROKER:
for TTN is it is included in the application handler 
	* topic:<AppID>/devices/<DevID>
	* +/devices/+/up(for messages sent from node 
	* +/devices/+/down(for messages receive by node)
	* +/devices/+/events/activations(communication activate of node)
	* +/devices/+/+(all things of communicate)
2. PORT:We generally use the port 1883
3. KEEP_ALIVE: 45 is good
4. ClientId: turn on your imagnation 
TTN
5. App_ID: the Name of your application on TTN(at the overview top  )
6. AccessKey: the access key of your application(at the overview bottom)
THINGS
7. URL: url of your ThingsBoard
8. PublicId: customers

  

