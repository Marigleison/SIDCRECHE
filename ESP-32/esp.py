import sys
from machine import Pin
from time import sleep
led = Pin(23, Pin.OUT)
botaoa = Pin(21, Pin.IN, Pin.PULL_DOWN)
botaob = Pin(19, Pin.IN, Pin.PULL_DOWN)
botaov = Pin(18, Pin.IN, Pin.PULL_DOWN)

while True:
    if botaoa.value() == 1:
        print('CRECHE1')
        led.value(1)
        sleep(0.5)
        led.value(0)
        sleep(0.5)
        
    if botaob.value() == 1:
        print('CRECHE2')
        led.value(1)
        sleep(0.5)
        led.value(0)
        sleep(0.5)
        
    if botaov.value() == 1:
        print('UNIFBV')
        led.value(1)
        sleep(0.5)
        led.value(0)
        sleep(0.5)