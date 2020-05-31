# Python file for detecting Joystick and Button Input.
import time

# Import GPIO (digital) and MCP3008 (analog) library.
import Adafruit_MCP3008
import Adafruit_GPIO as GPIO

gpio = GPIO.get_platform_gpio()
adapter = GPIO.RPiGPIOAdapter(gpio)
adapter.setup(2, GPIO.IN)
gpio.setup.assert_called_with(2, gpio.IN, pull_up_down=gpio.PUD_OFF)

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

    print('X: ' + str(jsx) + ', Y: ' + str(jsy) + ', Z: ' + gpio.input(2))
