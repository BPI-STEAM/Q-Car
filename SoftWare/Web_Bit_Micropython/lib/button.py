from time import time, sleep_ms, ticks_ms

class Button:

    def __init__(self, pin_id):
        from machine import Pin
        self.pin = Pin(pin_id, Pin.IN)
        self.old_time = ticks_ms()
        self.new_time = self.old_time
        self.irq = self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.__irq_sc)
        self.presses = 0
        self.pressed = False

    def __irq_sc(self, p):
        # print(self, p)
        self.new_time = ticks_ms()
        if (self.new_time - self.old_time) > 200:
            self.presses += 1
            self.pressed = True
            self.old_time = self.new_time
            
        #sleep_ms(10)

    def close(self):
       self.irq.trigger(0) 

    def reset(self):
       self.presses = 0

    def get_presses(self):
        r = self.presses
        self.presses = 0
        return r

    def is_pressed(self):
        return self.pin.value() == 0

    def was_pressed(self):
        r = self.pressed
        self.pressed = False
        return r

def unit_test():
    print('The unit test code is as follows')
    print('\n\
        button_a = Button(35)\n\
        while True:\n\
            print(\'button_a was_pressed \', button_a.was_pressed())\n\
            print(\'button_a is_pressed \', button_a.is_pressed())\n\
            print(\'button_a get_presses \', button_a.get_presses())\n\
        ')
    try:
        button_a = Button(35)
        while True:
            sleep_ms(100)
            print('button_a was_pressed ', button_a.was_pressed())
            print('button_a is_pressed ', button_a.is_pressed())
            print('button_a get_presses ', button_a.get_presses())
    finally:
        button_a.close()

if __name__ == '__main__':
    unit_test()

