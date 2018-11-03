import machine as mc
from time import sleep

touch0 = mc.TouchPad(mc.Pin(33))

while True:
    sleep(0.1)
    print(touch0.read())
