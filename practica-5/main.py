import bluetooth
from machine import Pin
from BLE import BLEUART

# Init LEDs
led = Pin(14, Pin.OUT)
led.off()

# Init Bluetooth
name = 'ESP32_nombre'
ble = bluetooth.BLE()
uart = BLEUART(ble, name)

# Bluetooth RX event
def on_rx():
    rx_buffer = uart.read().decode().strip()
    uart.write('ESP32 recibe: ' + str(rx_buffer) + '\n')

    if rx_buffer == 'on':
        led.on()
    if rx_buffer == 'off':
        led.off()

# Register Bluetooth event
uart.irq(handler=on_rx)
