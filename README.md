# gateWay_ttn-thingsboard
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
https://github.com/guiguitt/gateway_ttn-thingsboard/archive/master.zip
```
* or clone on your computer 
```
git clone https://github.com/guiguitt/gateway_ttn-thingsboard.git
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
pip3 install paho-mqtt
```
* requests
```
pip3 install requests
````
* json
* datatime
### Commissioning
- MQTT
1. BROKER:
for TTN is it is included in the application handler 
	* topic:<AppID>/devices/<DevID>
	* +/devices/+/up - for messages sent from node
	* +/devices/+/down - for messages receive by node
	* +/devices/+/events/activations - (communication activate of node
	* +/devices/+/+ - all things of communicate
2. PORT: We generally use the port 1883
3. KEEP_ALIVE: 45 is good
4. ClientId: turn on your imagnation 
- TTN
5. App_ID: the Name of your application on TTN (at the overview top )
6. AccessKey: the access key of your application (at the overview bottom)
- THINGS
7. URL: url of your ThingsBoard
8. PublicID: ->customers->copy customers ID
## script installation(In Progress...non-operational)------------------------------------------------------
## DDorch addition 

- add a user `gateway_ttn` on the server: `sudo adduser gateway_ttn`.
- clone the current repository in the home of this newly added user.
```
su gateway_ttn
cd
git clone https://github.com/guiguitt/gateway_ttn-thingsboard.git
exit
```
- configure the systemctl service by editing the file `/etc/systemd/system/gateway_ttn.service` as root
```
sudo nano /etc/systemd/system/gateway_ttn.service
```

The content of `/etc/systemd/system/gateway_ttn.service`: 

```
[Unit]
Description=Gateway between TTN and Thingsboard
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=gateway_ttn
ExecStart=/usr/bin/env python3 /home/gateway_ttn/gateway_ttn-thingsboard.py

[Install]
WantedBy=multi-user.ta
```

- Start the service: `sudo systemctl start`
- Check if the service is working properly: ` sudo systemctl status gateway_ttn.service`

```
gateway_ttn.service - Gateway between TTN and Thingsboard
   Loaded: loaded (/etc/systemd/system/gateway_ttn.service; disabled; vendor preset: enabled)
   Active: active (running) since Wed 2019-06-26 11:36:58 CEST; 8ms ago
 Main PID: 27385 (python3)
    Tasks: 0 (limit: 4915)
   CGroup: /system.slice/gateway_ttn.service
           └─27385 python3 /home/gateway_ttn/gateway_ttn-thingsboardpy
```

- enable service at startup with command 
````sudo systemctl enable gateway_ttn.service```


  

