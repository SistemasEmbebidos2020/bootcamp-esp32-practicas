from machine import Timer, Pin

import HCSR04

period = 100
maxDevice = 4
sensor = HCSR04.HCSR04(trigger_pin=5, echo_pin=18, echo_timeout_us=500 * 2 * 30)
led_rojo = Pin(27, Pin.OUT)
led_azul = Pin(14, Pin.OUT)
led_amarillo = Pin(26, Pin.OUT)
led_verde = Pin(12, Pin.OUT)


def timerEvent():
    distance = int(sensor.distance_cm())
    print("Distance: ", distance, " cm")
    if distance > 20:
        led_rojo.off()
        led_amarillo.off()
        led_azul.off()
        led_verde.on()
    elif distance <= 20 and distance > 15:
        led_rojo.off()
        led_amarillo.off()
        led_azul.on()
        led_verde.on()
    elif distance <= 15 and distance > 10:
        led_rojo.off()
        led_amarillo.on()
        led_azul.on()
        led_verde.on()
    else:
        led_rojo.on()
        led_amarillo.on()
        led_azul.on()
        led_verde.on()


tim1 = Timer(1)
tim1.init(period=period, mode=Timer.PERIODIC, callback=lambda t: timerEvent())

while True:
    pass
