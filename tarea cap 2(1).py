"Tarea cap 2"
from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)

contador=0
while True:
    if sw.value():
        contador += 1
        if contador == 10:
           led.value(not led.value()) 
           contador = 0
        print(contador)     
        time.sleep_ms(250)   
        