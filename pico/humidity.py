import machine
import dht
import time

humidity_pin = machine.Pin(2)
humidity_sensor = dht.DHT22(humidity_pin)

def getHumidity():
    return humidity_sensor.humidity()