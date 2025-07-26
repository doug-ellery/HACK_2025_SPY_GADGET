import machine
import utime

trig = machine.Pin(18, machine.Pin.OUT)  # Trigger pin
echo = machine.Pin(17, machine.Pin.IN)  # Echo pin

def measure_distance():
    trig.low() # Ensure trigger is low
    utime.sleep_us(2)  # Wait for 2 microseconds
    trig.high()
    utime.sleep_us(10)  # Send a 10 microsecond pulse
    trig.low()

    while echo.value() == 0:   # Wait for echo to go high
        pass
    start = utime.ticks_us()  # Record start time

    while echo.value() == 1:   # Wait for echo to go low
        pass
    end = utime.ticks_us()  # Record end time

    duration = utime.ticks_diff(end, start)
    distance = (duration * 0.0343) / 2 + 0.45172 # Calculate distance in cm (Speed of sound is 343 m/s)

    return distance