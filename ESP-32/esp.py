import sys
from machine import Pin
from time import sleep
led = Pin(23, Pin.OUT)
pinoa = Pin(21, Pin.IN, Pin.PULL_DOWN)
pinob = Pin(19, Pin.IN, Pin.PULL_DOWN)
pinoc = Pin(18, Pin.IN, Pin.PULL_DOWN)

while True:
    if pinoa.value() == 1:
        print('CRECHE1')
        led.value(1)
        sleep(0.5)
        led.value(0)
        sleep(0.5)
        
    if pinob.value() == 1:
        print('CRECHE2')
        led.value(1)
        sleep(0.5)
        led.value(0)
        sleep(0.5)
        
    if pinoc.value() == 1:
        print('UNIFBV')
        led.value(1)
        sleep(0.5)
        led.value(0)

        sleep(0.5)

