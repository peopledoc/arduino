int led = 11;
int car;

int lastStatus = LOW;

void setup(){
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if(Serial.available() > 0) {
    while(car = Serial.read() != 'O');
    if(lastStatus == LOW) lastStatus = HIGH;
    else lastStatus = LOW;
    digitalWrite(led, lastStatus);
  }
}
