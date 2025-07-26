import dht 
import time 
import machine

# Initialize DHT11 sensor on GPIO 16
d = dht.DHT11(machine.Pin(16))

# Continuously read and print temperature and humidity
def getTemp():
    d.measure()  # Trigger measurement
    farenheittemp = d.temperature() * 9.0 / 5.0 + 32 - 3  # Convert to Fahrenheit (Minus 6 from calibration)
    return farenheittemp  # Print temperature
