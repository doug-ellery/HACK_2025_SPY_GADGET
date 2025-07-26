import dht 
import time 
import machine

# Initialize DHT11 sensor on GPIO 16
d = dht.DHT11(machine.Pin(16))

# Continuously read and print temperature and humidity
def getHumidity():
    d.measure()  # Trigger measurement
    calibratedHumid = d.humidity() + 11
    return calibratedHumid