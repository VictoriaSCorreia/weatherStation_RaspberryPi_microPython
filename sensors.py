from machine import Pin
from machine import SoftI2C
from time import sleep
from bmp085 import BMP180
import dht

# led
led = Pin("LED", Pin.OUT)
# bmp
i2c = SoftI2C(sda = 0, scl = 1, freq = 100000)
bmp = BMP180(i2c)
bmp.oversample = 2
bmp.sealevel = 101325
# dht
sensorDht = dht.DHT11(Pin(2))

def measureData():
    sensorDht.measure()
    temperature = bmp.temperature # C°
    humidity = sensorDht.humidity() # %
    pressure = bmp.pressure  # hPa
    return temperature, humidity, pressure


while True:
    led.high()
    temperature, humidity, pressure = measureData()
    print(f"Temperature: {temperature}C°")
    print(f"Pressure: {pressure} hPa")
    print(f"Humidity: {humidity}%")
    led.low()
    sleep(4)
