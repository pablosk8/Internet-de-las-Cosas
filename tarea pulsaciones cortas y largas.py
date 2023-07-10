#  Tarea cap 2
from machine import Pin
import time

print("esperando pulsador")

sw = Pin(23, Pin.IN)
led = Pin(2, Pin.OUT)
contador=0

while True:
    if sw.value():
        contador += 1
        print(contador)
        if contador >= 600:
           print("pulsacion larga")
    else:
        if contador >=200 and contador <= 400:
            print("pulsacion corta")
        contador = 0   
        time.sleep_ms(1)   
        
