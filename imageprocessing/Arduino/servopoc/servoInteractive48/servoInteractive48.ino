#include <Servo.h>
int LIMIT=48;
String input = "";
Servo sArr[48];
void setup() {
  Serial.begin(9600);
  Serial.setTimeout(250);
  initServo();
}

void initServo(){
  sArr[0].attach(14);sArr[1].attach(15);sArr[2].attach(16);sArr[3].attach(17);sArr[4].attach(18);sArr[5].attach(19);sArr[6].attach(20);sArr[7].attach(21);
  sArr[8].attach(29);sArr[9].attach(28);sArr[10].attach(27);sArr[11].attach(26);sArr[12].attach(25);sArr[13].attach(24);sArr[14].attach(23);sArr[15].attach(22);
  sArr[16].attach(2);sArr[17].attach(3);sArr[18].attach(4);sArr[19].attach(5);sArr[20].attach(6);sArr[21].attach(7);sArr[22].attach(8);sArr[23].attach(9);
  sArr[24].attach(30);sArr[25].attach(31);sArr[26].attach(32);sArr[27].attach(33);sArr[28].attach(34);sArr[29].attach(35);sArr[30].attach(36);sArr[31].attach(37);
  sArr[32].attach(38);sArr[33].attach(39);sArr[34].attach(40);sArr[35].attach(41);sArr[36].attach(42);sArr[37].attach(43);sArr[38].attach(44);sArr[39].attach(45);
  sArr[40].attach(53);sArr[41].attach(52);sArr[42].attach(51);sArr[43].attach(50);sArr[44].attach(49);sArr[45].attach(48);sArr[46].attach(47);sArr[47].attach(46);
  
  for(int i = 0; i < 48 ; i++){
    //sArr[i].attach(i);
    sArr[i].write(0);
  }

}

void reset(){
  for(int i = 0; i < 48 ; i++){
    sArr[i].write(0);
  }
}

//void attachServos(){
//  for(int i = 0; i < 48 ; i++){
//    sArr[i].write(0);
//  } 
//}

void loop() {
  while(Serial.available() == 0){
//   for(int i = 0; i < 48 ; i++){
//    //sArr[i].attach(i);
//    sArr[i].write(0);
//  }
  }
  //Serial.println("");
  input = Serial.readString();
  
  //Serial.println(input);  
  if(input.length() < 48){
    reset();
  }else{
    writeToServos(input);
  }
  Serial.flush();    
  delay(100);
}

void writeToServos(String input){
  //Serial.println(input);
//  Serial.flush();
  for(int i = 0; i < 48 ; i++){
    if(input[i+1] == '1'){
     // Serial.println("OK");
      sArr[i].write(25);
      //delay(300);
    }else{
      sArr[i].write(0);
      //delay(100);
    } 
  }
}

//if(a[1] == '1'){
//    s2.write(45);
//    delay(150);
//    s2.write(0);
//    delay(150);
//  }
//  if(a[3] == '1'){
//    s2.write(45);
//    delay(150);
//    s2.write(0);
//  }

