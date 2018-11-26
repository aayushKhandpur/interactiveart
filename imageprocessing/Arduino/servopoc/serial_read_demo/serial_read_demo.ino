#include <Servo.h>

int LIMIT=48;
Servo s2;
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(250);
  s2.attach(2);
  s2.write(0);

}

void loop() {
  while(Serial.available() == 0){
    //Serial.print("NA");
  }
  String a = Serial.readString();
  Serial.flush();  
  if(a[1] == '1'){
    s2.write(45);
    delay(150);
    s2.write(0);
    delay(150);
  }
  if(a[3] == '1'){
    s2.write(45);
    delay(150);
    s2.write(0);
  }
  Serial.println("OK");
}

