from machine import I2C, Pin
from bmp180 import BMP180
import utime


# Inicializa a comunicação I2C com o ID 0, definindo os pinos SCL e SDA e a frequência de comunicação (100 kHz)
i2c = I2C(id=0, scl=Pin(1), sda=Pin(0), freq=100000)

bmp180 = BMP180(i2c)
# Define a configuração de oversampling para o sensor (maior valor significa maior precisão, mas mais tempo de leitura)
bmp180.oversample_sett = 2
# Define o valor de referência da pressão ao nível do mar em Pascal (101325 Pa)
bmp180.baseline = 101325

while True:
    p = bmp180.pressure
    print("Pressão:", p, "Pa")
    utime.sleep(5)
