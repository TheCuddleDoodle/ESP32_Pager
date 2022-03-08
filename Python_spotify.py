import requests,json
from requests.structures import CaseInsensitiveDict

url = "https://api.spotify.com/v1/me/player/currently-playing?market=ES"

headers = CaseInsensitiveDict()
headers["Accept"] = "application/json"
headers["Content-Type"] = "application/json"
headers["Authorization"] = "Bearer"

r = requests.get(url,headers=headers)
json_temp = r.text
# json_temp = json.loads(json_temp)
print(json_temp)
# print(data['name'])
def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('##', '##')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())
    
def spotify_conn():
  
