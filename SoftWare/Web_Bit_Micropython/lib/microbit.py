import machine

from utime import ticks_ms as running_time, sleep_ms as sleep

import pins
pin0 = pins.D_Pin(25)
pin1 = pins.A_Pin(32)
pin2 = pins.A_Pin(33)
pin3 = pins.D_Pin(13)
pin4 = pins.D_Pin(16)
pin5 = pins.D_Pin(35)
pin6 = pins.D_Pin(12)
pin7 = pins.D_Pin(14)
pin8 = pins.D_Pin(16)
pin9 = pins.D_Pin(17)
pin10 = pins.D_Pin(26)
pin11 = pins.D_Pin(27)
pin12 = pins.D_Pin(2)
pin13 = pins.D_Pin(18)
pin14 = pins.D_Pin(19)
pin15 = pins.D_Pin(23)
pin16 = pins.D_Pin(5)
pin19 = pins.D_Pin(22)
pin20 = pins.D_Pin(21)

def panic(flag=0):
    return machine.reset_cause()

reset = machine.reset

import display
Image = display.Image
display = display.Display()

import button
button_a = button.Button(35)
button_b = button.Button(27)

import temperature
__adc = machine.ADC(machine.Pin(34, machine.Pin.IN))
__adc.atten(machine.ADC.ATTN_11DB)
temperature = temperature.Temperature(__adc).temperature

try:
    from mpu9250 import MPU9250
    from mpu6500 import MPU6500
    __i2c = machine.I2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=200000)
    __dev = __i2c.scan()
    # print("dev ", __dev)
    if 104 in __dev:
        print("1.4 version")
        __sensor = MPU9250(__i2c, MPU6500(__i2c, 0x68))
    if 105 in __dev:
        print("1.2 version No compass")
        __sensor = MPU9250(__i2c, MPU6500(__i2c, 0x69))
    import accelerometer
    accelerometer = accelerometer.Direction(__sensor)
    import compass
    compass = compass.Compass(__sensor)
except Exception as e:
    print("MPU9250 Error", e)
