# Electrom Controller
Controller code for the electric trombone.

## Install dependencies
```
sudo apt install python3-pip
pip3 install adafruit-mcp3008
pip3 install RPi.GPIO
# sudo pip3 install adafruit-gpio
```

## Pair with laptop
```
sudo bluetoothctl
```

```
agent on
default-agent
scan on
list
pair XX:XX:XX:XX:XX:XX # the device to pair with.
```
