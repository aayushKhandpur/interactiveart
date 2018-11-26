#include <Servo.h>

Servo s2,s3,s4,s5,s6,s7,s8, s9;
int pin = 5;
int pos = 0;
int deg = 30;
int sPin = 0;
void setup() {
  Serial.begin(9600);
  s2.attach(2);s3.attach(3);s4.attach(4);s5.attach(5);s6.attach(6);s7.attach(7);s8.attach(8);s9.attach(9);
  s2.write(pos);s3.write(pos);s4.write(pos);s5.write(pos);s6.write(pos);s7.write(pos);s8.write(pos);s9.write(pos);
}

void loop() {  
 while(Serial.available() == 0){
  s2.write(pos);s3.write(pos);s4.write(pos);s5.write(pos);s6.write(pos);s7.write(pos);s8.write(pos);s9.write(pos); 
 }
 sPin = Serial.read();
 //s2.write(deg);s3.write(deg);s4.write(deg);s5.write(deg);s6.write(deg);s7.write(deg);s8.write(deg);s9.write(deg);
  if(sPin > 0 && sPin <=10){    
    s2.write(30);
  }else {
    s2.write(pos);
  }
  if(sPin > 10 && sPin <=20){    
    s3.write(30);
  }else {
    s3.write(pos);
  }
  if(sPin > 20 && sPin <=30){    
    s4.write(30);
  }else {
    s4.write(pos);
  }
  if(sPin > 30 && sPin <=40){    
    s5.write(30);
  }else {
    s5.write(pos);
  }
  if(sPin > 40 && sPin <=40){    
    s5.write(30);
  }else {
    s5.write(pos);
  }
  delay(100);
  //s2.write(pos);s3.write(pos);s4.write(pos);s5.write(pos);s6.write(pos);s7.write(pos);s8.write(pos);s9.write(pos);
 // delay(500);
}

