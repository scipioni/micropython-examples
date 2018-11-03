import machine as mc
from time import sleep

sleep(1)

wake = mc.Pin(34,mc.Pin.IN)

# GPIO22 is the internal LED for TTGO MINI32
led = mc.Pin(22, mc.Pin.OUT)


val = wake.value()
if val == 1:
    edge = mc.Pin.WAKE_LOW
else:
    edge = mc.Pin.WAKE_HIGH

wake.irq(trigger = edge , wake = mc.DEEPSLEEP)
print('value:{}, edge:{}'.format(val, edge))

led.value(not led.value())
sleep(1)
led.value(not led.value())


print('sleep ...')
mc.deepsleep()


