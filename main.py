import time
import machine

ldr1 = machine.Pin(4, machine.Pin.OUT)
ldr2 = machine.Pin(5, machine.Pin.OUT)

ldr1val = 0
ldr2val = 0

retning = 40

adc = machine.ADC(0)

servopin = machine.Pin(14)
servo = machine.PWM(servopin, freq=50)

ldr1.value(0)
ldr2.value(0)
servo.duty(retning)

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
        retning +=10
    elif (sammen <= -99):
        retning -=10
    else:
        retning +=0
    #    print("nothing to do")

    if (retning < 40):
        retning = 40
    elif (retning > 120):
        retning = 120
    else:
        retningt = retning

    servo.duty(retning)



    #print(retning)
    #print("-------------------------")
    time.sleep(2)
