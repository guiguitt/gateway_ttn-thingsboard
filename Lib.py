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
    printlog("send to ThingsBoard")
    headers_AcessT = {
          'Content-Type': 'application/json',
          'Accept': 'application/json',
            }
    ResponseAcessToken = requests.post(dPrm['THINGS']['url']+'/api/auth/login/public', headers=headers_AcessT, data=dPrm['THINGS']['publicid'])
    #printlog("ResponseAcessToken: "+ResponseAcessToken.text)
    AcessToken=eval(ResponseAcessToken.text)['token']
    headers_DeviceT = {
            'Accept': 'application/json',
            'X-Authorization': "Bearer " +AcessToken
            }
    ResponseDeviceToken = requests.get(dPrm['THINGS']['url']+'/api/device/'+DeviceId+'/credentials', headers=headers_DeviceT)
    #printlog("ResponseDeviceToken: "+str(ResponseDeviceToken.text))
    null = None
    DeviceToken=str(eval(ResponseDeviceToken.text)['credentialsId'])
    r = requests.post(dPrm['THINGS']['url']+'/api/v1/'+DeviceToken+'/telemetry', json=JsDATA)
    printlog("request code reponse:"+str(r))


def on_log( client, userdata, level, buf ):
    printlog( "log: "+ buf)

def on_connect( client, userdata, flags, rc ):
    printlog( "Connexion MQTT: code retour= "+ str(rc) )
    printlog( "Connexion MQTT: Statut= " +("OK" if rc==0 else "échec") )

def on_message( client, userdata, message ):
    printlog( "Recept message MQTT..." )
    printlog( "Topic : "+ str(message.topic) )
    msg = json.loads(message.payload)
    #printlog("dev_if : " +y["dev_id"])
    #printlog("Latitude: " +y["payload_fields"]["latitude"])    
    #printlog("Longitude: " +y["payload_fields"]["longitude"])    
    #printlog("detection: %s" +y["payload_fields"]["detection"])	
    printlog("data: "+str(msg["payload_fields"]))
    PostThingsboard(msg["payload_fields"], msg['dev_id'])