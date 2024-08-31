# SPDX-FileCopyrightText: Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import sys
import board
import digitalio
from PIL import Image
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
oled_reset = digitalio.DigitalInOut(board.D22)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed

#i2c = board.I2C()  # uses board.SCL and board.SDA
# i2c = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.
# Change these to the right size for your display!
#oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Note you can change the I2C address, or add a reset pin:
# oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3D, reset=oled_reset)

# Use for SPI
spi = board.SPI()
#oled_cs = digitalio.DigitalInOut(board.CS)
oled_cs = None;
oled_dc = digitalio.DigitalInOut(board.D18)
oled = adafruit_ssd1306.SSD1306_SPI(WIDTH, HEIGHT, spi, oled_dc, oled_reset, oled_cs)

# Clear display.
oled.fill(0)
oled.show()

# Open, resize, and convert image to Black and White
image = (
    Image.open(sys.argv[1])
    .resize((oled.width, oled.height), Image.BICUBIC)
    .convert("1")
)

# Display the converted image
oled.image(image)
oled.show()
