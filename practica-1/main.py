from machine import Pin
import time

led = Pin(2, Pin.OUT) 
led.on()

while(1):
    led.on()
    time.sleep_ms(500)  
    led.off()
    time.sleep_ms(500)
