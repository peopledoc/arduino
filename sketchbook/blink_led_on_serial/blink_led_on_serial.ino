int led = 11;
int car;

void setup(){
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if(Serial.available() > 0) {
    car = Serial.read();
    if(car == 'H') digitalWrite(led, HIGH);
    if(car == 'L') digitalWrite(led, LOW);
  }
}
