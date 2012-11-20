int button0 = A0;
int button1 = A1;
int button2 = A2;
int button3 = A3;

int led0 = 11;
int led1 = 10;
int led2 = 9;
int led3 = 6;

void setup(){
  // Prepare buttons
  pinMode(button0, INPUT);
  pinMode(button1, INPUT);
  pinMode(button2, INPUT);
  pinMode(button3, INPUT);
  
  // Prepare leds
  pinMode(led0, OUTPUT);
  pinMode(led1, OUTPUT);
  pinMode(led2, OUTPUT);
  pinMode(led3, OUTPUT);
}

void loop(){
  if(digitalRead(button0)){
    digitalWrite(led0, HIGH);
    wait();
  }
  if(digitalRead(button1)){
    digitalWrite(led1, HIGH);
    wait();
  }
  if(digitalRead(button2)){
    digitalWrite(led2, HIGH);
    wait();
  }
  if(digitalRead(button3)){
    digitalWrite(led3, HIGH);
    wait();
  }
}

void wait(){
  delay(5000);
  digitalWrite(led0, LOW);
  digitalWrite(led1, LOW);
  digitalWrite(led2, LOW);
  digitalWrite(led3, LOW);
   
}
