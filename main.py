import time
import machine

ldr1 = machine.Pin(4, machine.Pin.OUT)
ldr2 = machine.Pin(5, machine.Pin.OUT)

ldr1val = 0
ldr2val = 0

retning = 40

adc = machine.ADC(0)


ldr1.value(0)
ldr2.value(0)

mp1 = machine.Pin(12, machine.Pin.OUT)
mp2 = machine.Pin(13, machine.Pin.OUT)
mp3 = machine.Pin(15, machine.Pin.OUT)
mp4 = machine.Pin(3, machine.Pin.OUT)

mp1.value(0)
mp2.value(0)
mp3.value(0)
mp4.value(0)

def turnl():
    mp4.value(0)
    mp1.value(1)
    time.sleep_ms(25)
    mp1.value(1)
    mp2.value(1)
    time.sleep_ms(25)
    mp1.value(0)
    mp2.value(1)
    time.sleep_ms(25)
    mp2.value(1)
    mp3.value(1)
    time.sleep_ms(25)
    mp2.value(0)
    mp3.value(1)
    time.sleep_ms(25)
    mp3.value(1)
    mp4.value(1)
    time.sleep_ms(25)
    mp3.value(0)
    mp4.value(1)
    time.sleep_ms(25)
    mp4.value(1)
    mp1.value(1)
    time.sleep_ms(25)

def turnr():
    mp1.value(0)
    mp4.value(1)
    time.sleep_ms(25)
    mp4.value(1)
    mp3.value(1)
    time.sleep_ms(25)
    mp4.value(0)
    mp3.value(1)
    time.sleep_ms(25)
    mp3.value(1)
    mp2.value(1)
    time.sleep_ms(25)
    mp3.value(0)
    mp2.value(1)
    time.sleep_ms(25)
    mp2.value(1)
    mp1.value(1)
    time.sleep_ms(25)
    mp2.value(0)
    mp1.value(1)
    time.sleep_ms(25)
    mp1.value(1)
    mp4.value(1)
    time.sleep_ms(25)


#print(ldr1val, ldr2val)

while True:

    ldr1.value(1)
    ldr1val = adc.read()
    #print(ldr1val)
    ldr1.value(0)
    time.sleep_ms(100)

    ldr2.value(1)
    ldr2val = adc.read()
    #print(ldr2val)
    ldr2.value(0)
    time.sleep_ms(100)

    sammen = (ldr1val - ldr2val)
    #print(sammen)

    if (sammen >= 99):
        for i in range(20):
            turnr()
    elif (sammen <= -99):
        for i in range(20):
            turnl()
    else:
        pass
        
    mp1.value(0)
    mp4.value(0)

    #print("-------------------------")
    time.sleep_ms(100)
