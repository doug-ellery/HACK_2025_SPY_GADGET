import ssd1306

i2c = SoftI2C(scl=Pin(1), sda=Pin(0))
oled_width = 128
oled_height = 64

oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)
oled.text('Hello, World 1!', 0, 0) # Display text on first line
oled.text('Hello, World 2!', 0, 10) # Display text on second line
oled.text('Hello, World 3!', 0, 20) # Display text on third line
oled.show() # Update the display to show the text