from machine import Pin, ADC, DAC, PWM

class D_Pin(Pin):

    def __init__(self, pin):
        self.pin = pin
        self.pwm = None
        self.io = Pin(pin)
        
    def write_digital(self, v):
        if self.pwm is not None:
            self.pwm.deinit()
            self.pwm = None
        self.io.init(Pin.OUT) # set pin as output
        self.io.value(v)

    def read_digital(self):
        if self.pwm is not None:
            self.pwm.deinit()
            self.pwm = None
        self.io.init(Pin.IN) # set pin as input
        return self.io.value()

    def write_analog(self, value):
        if self.pwm is None:
            self.pwm = PWM(self.io, freq=1000)
            #self.pwm.freq(10000)
        self.pwm.duty(value)

    def time_pules_in(level, timeout):
        if self.io is None:
            self.io = super()

class A_Pin(D_Pin):
    
    def __init__(self, pin):
        #self.pin = pin
        self.dac = None
        self.adc = None
        if pin in [25,26]:
            self.dac = DAC(Pin(pin))
        if pin in [32,33]:
            self.adc = ADC(Pin(pin))
            self.adc.atten(ADC.ATTN_11DB)
            self.adc.width(ADC.WIDTH_10BIT)
        super().__init__(pin)
    
    def write_analog(self, value):
        if self.pin not in [25,26]:
            # print("This pin feature is not supported")
            super().write_analog(value)
        else:
            self.dac.write(value)

    def read_analog(self):
        if self.adc != None:
            return self.adc.read()
        else:
            print('This Pin does not support ADC')
            return None

class T_Pin(A_Pin):
    
    def __init__(self, pin):
        super().__init__(pin)
    
    def is_touched(self):
        return self.read_analog() > 100

def unit_test():
    from utime import sleep_ms as sleep
    pin13 = D_Pin(18) # PWR_LED
    pin1 = T_Pin(32)
    pin2 = T_Pin(33)
    pin10 = A_Pin(26)
    pin5 = D_Pin(35)  # Button_A
    pin14 = D_Pin(19)
    pin15 = D_Pin(23)
    while True:
        pin13.write_digital(1)
        sleep(50)
        pin13.write_digital(0)
        sleep(50)
        print('Please press P1')
        sleep(100)
        #print('pin1(P1).is_touched()', pin1.is_touched())
        sleep(100)
        print('Please press A')
        sleep(100)
        print('Button_A.read_digital()', pin5.read_digital())
        print('the ADC P2 values is ', pin2.read_analog())
        print('Seting P14 to 128')
        pin14.write_analog(0)
        print('Seting P15 to 128')
        pin15.write_analog(0)
        sleep(15)
        print('Seting P14 to 1023')
        pin14.write_analog(1023)
        print('Seting P15 to 1023')
        pin15.write_analog(1023)
        #for val in range(150,255,1):
        #    pin10.write_analog(val)
        #    sleep(10)
        #for val in range(255,150,-1):
        #    pin10.write_analog(val)
        #    sleep(10)

        

if __name__ == '__main__':
    unit_test()

