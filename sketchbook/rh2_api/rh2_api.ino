// Define the number of leds.
const int NB_LEDS = 4;
const int START_BYTE = '~'; // 126

unsigned long startTrigger[NB_LEDS];
unsigned long totalTime[NB_LEDS];
unsigned long onTime[NB_LEDS];
unsigned long offTime[NB_LEDS];

unsigned long currentTime;
int led;
int i;

unsigned long currentStatus, periodTime, currentPeriod, periodStartTime;

int leds[] = {11, 10, 9, 6, 5, 3};

void setup(){
  for(i = 0; i < NB_LEDS; i++){
    pinMode(leds[i], OUTPUT);
    totalTime[i] = 0;
    onTime[i] = 0;
    offTime[i] = 0;
  }
  
  Serial.begin(9600);
}

void loop(){
  // Read the serial port and configure the event
  
  if(Serial.available() > 0) {
    if(Serial.read() == START_BYTE){ // Flush the Serial until we find a start byte.
      led = Serial.read();
      if(led < 0 || led > 6) return;
      totalTime[led] = Serial.read() * 100;
      onTime[led] = Serial.read() * 10;
      offTime[led] = Serial.read() * 10;
      startTrigger[led] = millis();
      digitalWrite(leds[led], HIGH);
      Serial.print(millis());
      Serial.print(' ');
      Serial.println(led);
    }
  }
  
  // For each led, activate/deactivate the led
  for(led = 0; led < NB_LEDS; led++){
    currentTime = millis();
    // If totalTime is expired : turn off the led
    if(currentTime > startTrigger[led] + totalTime[led]) {
      digitalWrite(leds[led], LOW);
    } else {
      // Time lapsed since the animation start
      // currentStatus = currentTime - startTrigger[led];
      
      // Time of on animation period
      periodTime = onTime[led] + offTime[led];
      
      // In which period are we ? 1, 2 ,3 ...
      currentPeriod = (currentTime - startTrigger[led]) / periodTime;
      
      // When did the period starts ?
      periodStartTime = startTrigger[led] + currentPeriod * periodTime;
      
      // Are we in the On part or the Off part ?
      if ((currentTime - periodStartTime) > onTime[led]) 
        digitalWrite(leds[led], LOW);
      else 
        digitalWrite(leds[led], HIGH);
    }
  }
  delay(10);
}
