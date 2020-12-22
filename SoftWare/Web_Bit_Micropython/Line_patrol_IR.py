import microbit as m

right_IR = 0
left_IR = 0

def Line_patrol_IR():
    global right_IR,left_IR #Declare global variables
    while True:
        m.pin14.write_digital(1)#pin14 controls the infrared pair tube, high level conduction
        right_IR = m.pin1.read_analog()#Pin1 receives the analog value of the right infrared pair tube voltage (0-1023)
        left_IR = m.pin2.read_analog()#pin2 receives the analog value of the left infrared pair tube voltage (0-1023)
        print("R:" + str(right_IR), "L:" + str(left_IR))#Serial port output left and right infrared pair tube voltage analog value
        m.sleep(100)#Delay 100ms

Line_patrol_IR()