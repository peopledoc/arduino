int led = 11;

int dot = 250;
int dash = 750;

void setup(){
  pinMode(led, OUTPUT);
}

void loop(){
  // S
  blink_led(dot);
  blink_led(dot);
  blink_led(dot);
  // O
  blink_led(dash);
  blink_led(dash);
  blink_led(dash);
  // S
  blink_led(dot);
  blink_led(dot);
  blink_led(dot);
  delay(1000);
}

void blink_led(int delay_wait) {
   digitalWrite(led, HIGH);
   delay(delay_wait);
   digitalWrite(led, LOW); 
   delay(delay_wait);
  
}
