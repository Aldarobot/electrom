#!/usr/bin/python3

# Python file for detecting Joystick and Button Input.
import time

# Import GPIO (digital) and MCP3008 (analog) library.
import Adafruit_MCP3008
import Adafruit_GPIO as GPIO

gpio = GPIO.get_platform_gpio()
adapter = GPIO.RPiGPIOAdapter(gpio)
adapter.setup(2, GPIO.IN)
gpio.setup.assert_called_with(2, gpio.IN, pull_up_down=gpio.PUD_OFF)

print("Starting...")

gpio = GPIO.get_platform_gpio()

print("Starting 2...")

# adapter = GPIO.RPiGPIOAdapter(gpio)
# print("Starting 3...")
# adapter.setup(2, GPIO.IN)

gpio.setup(2, GPIO.IN)

# print("Starting 4...")
 
#gpio.setup.assert_called_with(2, gpio.IN, pull_up_down=gpio.PUD_OFF)

print("Starting 5...")

# Software SPI configuration:
CLK  = 11
MISO = 9 # DOUT
MOSI = 10 # DIN
CS   = 8
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Main program loop.
while True:
    # Detect X Axis
    jsx = mcp.read_adc(0)

    # Detect Y Axis
    jsy = mcp.read_adc(1)

    print('X: ' + str(jsx) + ', Y: ' + str(jsy) + ', Z: ' + str(gpio.input(2)))
