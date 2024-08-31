# SPDX-FileCopyrightText: 2021 Melissa LeBlanc-Williams for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!
#
# Ported to Pillow by Melissa LeBlanc-Williams for Adafruit Industries from Code available at:
# https://learn.adafruit.com/adafruit-oled-displays-for-raspberry-pi/programming-your-display

# Imports the necessary libraries...
import board
import digitalio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

# Setting some variables for our reset pin etc.
oled_reset = digitalio.DigitalInOut(board.D22)

# Change these
# to the right size for your display!
WIDTH = 128
HEIGHT = 64  # Change to 64 if needed

# Very important... This lets py-gaugette 'know' what pins to use in order to reset the display
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

# Create blank image for drawing.
image = Image.new("1", (oled.width, oled.height))
draw = ImageDraw.Draw(image)

# Load a font in 2 different sizes.
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 14)

# Draw the text
draw.text((0, 0), "Hello!", font=font, fill=255)
draw.text((0, 30), "Hello!", font=font2, fill=255)
draw.text((34, 46), "Hello!", font=font2, fill=255)

# Display image
oled.image(image)
oled.show()
