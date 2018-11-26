#include <Servo.h>

Servo s2;
Servo s3;
Servo s4;
Servo s5;
Servo s6;
Servo s7;
int incomingByte = 0;
int pin = 9;
void setup() {
 // Serial.begin(9600);
  // put your setup code here, to run once:
  s2.attach(2);s3.attach(3);s4.attach(4);s5.attach(5);s6.attach(6);s7.attach(7);
}

void loop() {
//  incomingByte = Serial.read();
//  if (Serial.available() > 0) {
//    // read the incoming byte:
//    incomingByte = Serial.read();
//    // say what you got:
//    Serial.print("I received: ");
//    Serial.println(incomingByte, DEC);
//  }
//   put your main code here, to run repeatedly:
//  s2.write(0);s3.write(0);s4.write(0);s5.write(0);s6.write(0);s7.write(0);
//  delay(1000);  
//  s2.write(180);s3.write(180);s4.write(180);s5.write(180);s6.write(180);s7.write(180);
//  delay(500);
//  s2.write(90);s3.write(90);s4.write(90);s5.write(90);s6.write(90);s7.write(90);
//  delay(500);
//  s2.write(30);s3.write(30);s4.write(30);s5.write(30);s6.write(30);s7.write(30);
//  delay(500);
}
