int led = 11;
int button = A0;

int lastState = LOW;

void setup(){
  pinMode(led, OUTPUT);
  pinMode(button, INPUT);
}

void loop(){
   if(digitalRead(button)) {
      digitalWrite(led, HIGH);
      while (digitalRead(button));
      digitalWrite(led, LOW);
   }
}
