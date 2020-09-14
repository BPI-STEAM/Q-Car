/*************************************************** 
 * Ultrasonic_Test.ino (Version 0.0.1)
 * This is a ultrasonic sensor test example for our Banana Pi Q-car
 * Copyright (C) 2020 Banana Pi Open Source STEAM education Group
 * https://github.com/BPI-STEAM
 * 2020/09/13
 ****************************************************/
const int TrigPin = P12; // Trigger Pin of Ultrasonic Sensor is P12
const int EchoPin = P14; // Echo Pin of Ultrasonic Sensor is P14

void setup() {
   Serial.begin(9600); // Starting Serial Terminal
}

void loop() {
   long duration, inches, cm;
   pinMode(TrigPin, OUTPUT);
   digitalWrite(TrigPin, LOW);
   delayMicroseconds(2);
   digitalWrite(TrigPin, HIGH);
   delayMicroseconds(10);
   digitalWrite(TrigPin, LOW);
   pinMode(EchoPin, INPUT);
   duration = pulseIn(EchoPin, HIGH);
   inches = microsecondsToInches(duration);
   cm = microsecondsToCentimeters(duration);
   Serial.print(inches);
   Serial.print("in, ");
   Serial.print(cm);
   Serial.print("cm");
   Serial.println();
   delay(100);
}

long microsecondsToInches(long microseconds) {
   return microseconds / 74 / 2;
}

long microsecondsToCentimeters(long microseconds) {
   return microseconds / 29 / 2;
}
