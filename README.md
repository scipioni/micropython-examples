
If you are putting MicroPython on for the first time then you should first erase the entire flash


Makefile
```
PORT := /dev/ttyUSB1

erase:
	esptool.py --chip esp32 --port $(PORT) erase_flash

upload-firmware:
	esptool.py --chip esp32 --port $(PORT) write_flash -z 0x1000 esp32-20181103-v1.9.4-683-gd94aa577a.bin

console:
	picocom $(PORT) -b115200
```


Upload script
```
PORT=/dev/ttyUSB1

blink:
	ampy -p $(PORT) put blink.py /main.py

```
