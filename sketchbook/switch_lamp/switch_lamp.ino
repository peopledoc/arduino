int led = 11;
int car;

int lastStatus = LOW;

void setup(){
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  Serial.print('Restart')
}

void loop(){
  if(Serial.available() > 0) {
    car = Serial.read();
    if(car == 'r') {
        if(lastStatus == LOW) lastStatus = HIGH;
        else lastStatus = LOW;
        digitalWrite(led, lastStatus);
    } else {
      Serial.print(car); 
    }
    while(Serial.available()) Serial.read(); // Flush the Serial
  }
}
