char buffer[10] = {0,0,0,0,0,0,0,0,0,0};
void setup(){
    Serial.begin(9600);
}
void loop(){
  while(Serial.available() > 0){
    Serial.println("ÖUTPUT");
    Serial.print(Serial.read());
  Serial.print(Serial.read());  
  }
  
}
