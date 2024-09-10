from machine import Pin, PWM, Timer

# variables
led = 1
period = 50
frecuency = 500
duty = 1023
dutyOff = 1023

# Configuración de pines
pwm13 = PWM(Pin(13))
pwm12 = PWM(Pin(12))
pwm14 = PWM(Pin(14))

pwm13.freq(frecuency) 
pwm12.freq(frecuency) 
pwm14.freq(frecuency) 

pwm13.duty(dutyOff) 
pwm12.duty(dutyOff) 
pwm14.duty(dutyOff)

def setLed():
    global led
    global duty
    global dutyOff

    duty -= 10
    if duty < 0:
        duty = dutyOff
        led += 1
        if led > 3:
            led = 1
    
    if led == 1:
        pwm13.duty(duty) 
        pwm12.duty(dutyOff) 
        pwm14.duty(dutyOff) 
        
    if led == 2:
        pwm13.duty(dutyOff) 
        pwm12.duty(duty) 
        pwm14.duty(dutyOff) 
        
    if led == 3:
        pwm13.duty(dutyOff) 
        pwm12.duty(dutyOff) 
        pwm14.duty(duty)

#set timer
timer1 = Timer(1)
timer1.init(period=period, 
   mode=Timer.PERIODIC, 
   callback=lambda t: setLed())