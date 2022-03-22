import requests,json
from requests.structures import CaseInsensitiveDict
import network
import machine as m
import socket
import time
import urequests as request
import json
from machine import SoftI2C, Pin
from i2c_lcd import I2cLcd


I2C_ADDR = 0x27
totalRows = 2
totalColums =16
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=10000) 

headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer BQC7WwB1zE-EzcHU8BvfazS6sllFDRT50Cqa32rHSSS_TIHY4vwIaqyf6IXEnrMvELpVyw3n9TpKt6BXSGvYVzyyB_KM_1Ll442fC7zgCwyoK0dInq4VtRfUP7owNTPNjXXFHk67AzU6w9YQHkqzkPFq9vTRxgEgj9ne',
}

lcd = I2cLcd(i2c, I2C_ADDR, totalRows, totalColums)

while(sta_if.isconnected()):
	response = request.get('https://api.spotify.com/v1/me/player/currently-playing', headers=headers)
	data = json.load(response.text)
	lcd.putstr(data['item']['name'])
	lcd.clear()


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
  
