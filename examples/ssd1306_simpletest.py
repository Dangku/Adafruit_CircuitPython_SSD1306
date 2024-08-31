# SPDX-FileCopyrightText: Tony DiCola
# SPDX-License-Identifier: CC0-1.0

# Basic example of clearing and drawing pixels on a SSD1306 OLED display.
# This example and library is meant to work with Adafruit CircuitPython API.

import board
import digitalio
import adafruit_ssd1306

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed

# Create the I2C bus interface.
#i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = busio.I2C(board.GP1, board.GP0)    # Pi Pico RP2040

# Create the SSD1306 OLED class.
#display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)
# You can change the I2C address with an addr parameter:
# display = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x31)

# Use for SPI
spi = board.SPI()
#cs = digitalio.DigitalInOut(board.CS)
cs = None;
dc = digitalio.DigitalInOut(board.D18)
reset = digitalio.DigitalInOut(board.D22)
display = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, dc, reset, cs)

# fills display with black pixels clearing it
display.fill(0)
display.show()

# Set a pixel in the origin 0,0 position.
display.pixel(0, 0, 1)
# Set a pixel in the middle 64, 16 position.
display.pixel(64, 16, 1)
# Set a pixel in the opposite 127, 31 position.
display.pixel(127, 31, 1)
display.show()
