from machine import Pin
from machine import I2C
import time

from pico_i2c_lcd import I2cLcd
from lcd_api import LcdApi

import dht
#configuração LCD#
sda=Pin(0)
scl=Pin(1)
i2c=I2C(0,sda=sda, scl=scl, freq=400000)
endereco = 0x27
linhas = 2
colunas = 16
lcd = I2cLcd(i2c,endereco,linhas,colunas)
#configuração DHT11#
sensorDht = dht.DHT11(Pin(2))

def medirDados():
    sensorDht.measure()
    temperatura = sensorDht.temperature()
    umidade = sensorDht.humidity()
    
    return temperatura, umidade


lcd.putstr("Iniciando")
lcd.move_to(0,1)
lcd.putstr("Medicao")
time.sleep(4)
while True:
    temperatura,umidade = medirDados()
    
    #Põe as informações no LCD
    lcd.move_to(0,0)
    lcd.putstr(f"Temperatura:{temperatura}C")
    lcd.move_to(0,1)
    lcd.putstr(f"umidade:{umidade}%")
    time.sleep(6)
