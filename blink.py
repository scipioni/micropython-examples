from machine import Pin
from time import sleep

# GPIO22 is the internal LED for TTGO MINI32
led = Pin(22, Pin.OUT)

# The internal LED turn on when the pin is LOW
while True:
    led.value(not led.value())
    sleep(1)
