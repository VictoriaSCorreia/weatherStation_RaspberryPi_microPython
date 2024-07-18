from machine import Pin
from machine import I2C
import time

from pico_i2c_lcd import I2cLcd
from lcd_api import LcdApi

import dht

# LCD configuration
sda=Pin(0)
scl=Pin(1)
i2c=I2C(0,sda=sda, scl=scl, freq=400000)
endereco = 0x27
linhas = 2
colunas = 16
lcd = I2cLcd(i2c,endereco,linhas,colunas)

# DHT11 configuration

sensorDht = dht.DHT11(Pin(2))

def measureData():
    sensorDht.measure()
    temperature = sensorDht.temperature()
    humidity = sensorDht.humidity()
    
    return temperature, humidity

