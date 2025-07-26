from machine import Pin, ADC
import time

adc = ADC(Pin(26))

def getLight():
    adcvalue = adc.read_u16()
    lumens = -((adcvalue-63500)/61150.0)
    return lumens
    