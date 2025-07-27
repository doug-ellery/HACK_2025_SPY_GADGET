import ssd1306
from machine import Pin,SoftI2C
import time

i2c = SoftI2C(scl=Pin(1), sda=Pin(0))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
def display(message):
    allWords = message.split()
    for i in range(0,len(allWords),5):
        oled.fill(0)
        oled.text(allWords[i], 0, 0) # Display text on first line
        if i+1 < len(allWords):
            oled.text(allWords[i+1], 0, 10) # Display text on second line
        if i+2<len(allWords):
            oled.text(allWords[i+2], 0, 20) # Display text on third line
        if i+3<len(allWords):
            oled.text(allWords[i+3], 0, 30)
        if i+4<len(allWords):
            oled.text(allWords[i+4], 0, 40)
        oled.show() # Update the display to show the text
        time.sleep(4)
    
    oled.fill(0)

    
    