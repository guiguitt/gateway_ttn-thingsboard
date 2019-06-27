import json
import requests
from datetime import datetime
import sys

def getIniParameters(sFile):
    """
    Read parameters in ini file
    @param sFile Paht to the ini file to read
    @return Dictionary with sections and parameters contained in the INI file
    """
    import os,sys
    sCurrentPath = os.path.abspath(os.path.dirname(sys.argv[0]))
    os.chdir(sCurrentPath)
    sIniFile = sFile
    import configparser as cp
    cfg = cp.ConfigParser()

    with open(sIniFile) as f:
        cfg.read_file(f)

    # https://stackoverflow.com/a/28990982
    return {s:dict(cfg.items(s)) for s in cfg.sections()}

def printlog(s, sep = ": "):
    """
    Print message with date and time and flush the console
    @see https://www.turnkeylinux.org/blog/unix-buffering
    """
    sDateTime = datetime.now().strftime("%Y/%m/%d %H:%M:%S")
    print(sDateTime + sep + s)
    sys.stdout.flush()
    
def PostThingsboard( JsDATA, DeviceId ):
    """
    performs queries on the Things Board API to be able to post the passed data as a parameter. 
        1. it requests token access with the publicId
        2. it requests the device token with access token and the deviceID pass as parameter  
        3. it posts the data to pass as a parameter with the device token
        @param dictionary: that contains the name of the data and the data
               DeviceID: the name of the device on TTN and the device ID on Thingsboard

    """
    printlog("send to ThingsBoard")
    headers_AcessT = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
            }
    
    try:
        printlog("1/9 - send request to Acess Token")
        ResponseAcessToken = requests.post(dPrm['THINGS']['url']+'/api/auth/login/public', headers=headers_AcessT, data=dPrm['THINGS']['publicid'])
        printlog("2/9 - Request response: " + ResponseAcessToken.text)
    except Exception as e:
        printlog("Request response: " + ResponseAcessToken.text)
        return
        
    printlog("3/9 - done")
    AcessToken=eval(ResponseAcessToken.text)['token']
    
    headers_DeviceT = {
            'Accept': 'application/json',
            'X-Authorization': "Bearer " +AcessToken
            }
    
    try:
        printlog("4/9 - send request to Device token")
        ResponseDeviceToken = requests.get(dPrm['THINGS']['url']+'/api/device/'+DeviceId+'/credentials', headers=headers_DeviceT)
        printlog("5/9 - Request response: " + ResponseAcessToken.text)
    except Exception as e:
        printlog("Request response: " + ResponseAcessToken.text)
        return
    printlog("6/9 - done")
    
    null = None
    DeviceToken=str(eval(ResponseDeviceToken.text)['credentialsId'])
    
    
    
    try:
        printlog("7/9 - send request telemetry" )
        r = requests.post(dPrm['THINGS']['url']+'/api/v1/'+DeviceToken+'/telemetry', json=JsDATA)
        printlog("8/9 - request code reponse:"+str(r.text))
    except Exception as e:
        printlog("Request response: " + r.text)
        return  
    printlog("9/9 - done")


def on_log( client, userdata, level, buf ):
    printlog( "log: "+ buf)

def on_connect( client, userdata, flags, rc ):
    printlog( "Connexion MQTT: code retour= "+ str(rc) )
    printlog( "Connexion MQTT: Statut= " +("OK" if rc==0 else "echec") )

def on_message( client, userdata, message ):
    """
    application that processes data when a message is 
    received and starts the post procedure on ThingsBoard
    """
    printlog( "Recept message MQTT..." )
    printlog( "Topic : "+ str(message.topic) )
    msg = json.loads(message.payload.decode("utf-8" ))
    #printlog("dev_if : " +y["dev_id"])
    #printlog("Latitude: " +y["payload_fields"]["latitude"])    
    #printlog("Longitude: " +y["payload_fields"]["longitude"])    
    #printlog("detection: %s" +y["payload_fields"]["detection"])	
    printlog("data: "+str(msg["payload_fields"]))
    PostThingsboard(msg["payload_fields"], msg['dev_id'])