import json
import requests
import time
requests.packages.urllib3.disable_warnings()



#-----------------Check Status--Loop-back------
def CheckLoopback():

    api_url = "https://10.0.15.101/restconf/data/ietf-interfaces:interfaces-state/interface=Loopback62070021"
    headers = { "Accept": "application/yang-data+json", 
                "Content-type":"application/yang-data+json"
              }
    basicauth = ("admin", "cisco")
    resp = requests.get(api_url, auth=basicauth, headers=headers, verify=False)

    if resp.status_code == 404:
        message_1 = "Loopback62070021 - Operational status is down"
    else:
        response_json = resp.json()
        message_1 = "Loopback62070021 - Operational status is " + response_json["ietf-interfaces:interface"]["oper-status"]

    return message_1
#-----------------------------------------------

#-----------------API-Chat---------------#
access_token = "ZDI3ZThjOGYtYjI4ZS00MGM4LTliZmEtMDQwNDA4MWYwMjgyMWNhY2RiODItODI3_P0A1_9a8a306f-5965-407f-a4b3-63b85af39c54"
room_id = 'Y2lzY29zcGFyazovL3VzL1JPT00vNjUwODkzMjAtY2QxOS0xMWVjLWE1NGUtNGQ2MmNhMWM4YmVl'
url = "https://webexapis.com/v1/messages"
Webex_headers = {
    'Authorization' : 'Bearer {}'.format(access_token),
    'Content-Type': 'application/json'
    }
Getparams = {'roomId': room_id, 'max': 1}
#-------------------------------------------#

#-------------Chat-----------#
def ChatWebex():
    while True:
        res = requests.get(url, headers=Webex_headers, params=Getparams).json()
        if res["items"][0]["text"] == "62070021":
            Postparams = {
                "roomId": room_id,
                "text": CheckLoopback()
            }
            res = requests.post(url, headers=Webex_headers, json=Postparams)
        print("Recieve Msg : " + res["items"][0]["text"])
        time.sleep(1)

ChatWebex()
#-----------------Chat---------------#