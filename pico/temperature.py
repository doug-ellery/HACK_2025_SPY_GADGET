import machine
import dht
import time

temp_pin = machine.Pin(2)
temp_sensor = dht.DHT22(temp_pin)

def getTemp():
    return temp_sensor.temperature()