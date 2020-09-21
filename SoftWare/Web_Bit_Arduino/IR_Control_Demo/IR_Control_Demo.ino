/*************************************************** 
 * IR_Control_Demo.ino (Version 0.0.1)
 * This is a Tracing example for our Banana Pi Q-car
 * We refer to the code from adafruint
 * If you want to use this code, you need to download the following libraries:
 * https://github.com/adafruit/Adafruit-PWM-Servo-Driver-Library
 * https://github.com/z3t0/Arduino-IRremote
 * Copyright (C) 2020 Banana Pi Open Source STEAM education Group
 * https://github.com/BPI-STEAM
 * 2020/09/13
 *  PCA9685
 * LED0&LED1    Right Motor
 * LED2&LED3    Left Motor
 * IR_Receove   P15
 ****************************************************/


/*************************************************** 
 *  PCA9685       Q-Car
 * LED0&LED1    Right Motor
 * LED2&LED3    Left Motor
 ****************************************************/
#include <IRremote.h>
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>
//The I2C address of PCA9685 is 0x5F
Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver(0x5F);

int RECV_PIN = P15;
IRrecv irrecv(RECV_PIN);
decode_results results;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver

  pwm.begin();
  pwm.setPWMFreq(1000);  // Set to whatever you like, we don't use it in this demo!

  // if you want to really speed stuff up, you can go into 'fast 400khz I2C' mode
  // some i2c devices dont like this so much so if you're sharing the bus, watch
  // out for this!
  Wire.setClock(400000);
}

void stop()
{
  pwm.setPWM(0, 4096, 0);       // turns pin fully on
  pwm.setPWM(1, 4096, 0);       // turns pin fully on
  pwm.setPWM(2, 4096, 0);       // turns pin fully on
  pwm.setPWM(3, 4096, 0);       // turns pin fully on
}
void foward()
{
  pwm.setPWM(0, 4096, 0);       // turns pin fully on
  pwm.setPWM(1, 0, 4096);       // turns pin fully off
  pwm.setPWM(2, 0, 4096);       // turns pin fully off
  pwm.setPWM(3, 4096, 0);       // turns pin fully on
}
void back()
{
  pwm.setPWM(0, 0, 4096);       // turns pin fully off
  pwm.setPWM(1, 4096, 0);       // turns pin fully on
  pwm.setPWM(2, 4096, 0);       // turns pin fully on
  pwm.setPWM(3, 0, 4096);       // turns pin fully off
}
void left()
{
  pwm.setPWM(0, 4096, 0);       // turns pin fully on
  pwm.setPWM(1, 0, 4096);       // turns pin fully off
  pwm.setPWM(2, 4096, 0);       // turns pin fully on
  pwm.setPWM(3, 0, 4096);       // turns pin fully off
}
void right()
{
  pwm.setPWM(0, 0, 4096);       // turns pin fully off
  pwm.setPWM(1, 4096, 0);       // turns pin fully on
  pwm.setPWM(2, 0, 4096);       // turns pin fully on
  pwm.setPWM(3, 4096, 0);       // turns pin fully off
}

void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    if (results.value == 0xFF18E7) // Receive the value
    {
       foward();
    } else if (results.value == 0xFF4AB5) //You can change the value here according to your IR Remote Controller
    {
       back();
    }
    else if (results.value == 0xFF10EF) //You can change the value here according to your IR Remote Controller
    {
       left();
    }
    else if (results.value == 0xFF5AA5) 
    {
       right();
    }else if (results.value == 0xFF38C7)
    {
       stop();
    }
    irrecv.resume(); // Receive the next value
  }
  delay(100);
}
