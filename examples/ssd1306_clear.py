# SPDX-FileCopyrightText: Tony DiCola
# SPDX-License-Identifier: CC0-1.0

# Basic example of clearing and drawing pixels on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.

# Import all board pins.
import board
import digitalio
import adafruit_ssd1306

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed

# Create the I2C interface.
#i2c = board.I2C()

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!
#display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
# Alternatively you can change the I2C address of the device with an addr parameter:
# display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x31)

# Use for SPI
spi = board.SPI()
#cs = digitalio.DigitalInOut(board.CS)
cs = None;
dc = digitalio.DigitalInOut(board.D18)
reset = digitalio.DigitalInOut(board.D22)
display = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, dc, reset, cs)

# Clear the display.  Always call show after changing pixels to make the display
# update visible!
display.fill(0)
display.show()
