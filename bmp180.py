from machine import I2C, Pin
from bmp180 import BMP180
import utime

i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=100000)

# Inicializa a comunicação I2C com o ID 0, definindo os pinos SCL e SDA e a frequência de comunicação (100 kHz)
bmp180 = BMP180(i2c)
bmp180.oversample_sett = 2
bmp180.baseline = 101325
while True:
    p = bmp180.pressure
    print("Pressão:", p, "Pa")
    utime.sleep(5)
