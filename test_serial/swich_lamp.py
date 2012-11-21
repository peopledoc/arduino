"""Make a serial led.

int led = 11;
int car;

int lastStatus = LOW;

void setup(){
  pinMode(led, OUTPUT);
  Serial.begin(9600);
}

void loop(){
  if(Serial.available() > 0) {
    car = Serial.read();
    if(car == 'H') {
        if(lastStatus == LOW) lastStatus = HIGH;
        else lastStatus = LOW;
        digitalWrite(led, lastStatus);
    }
  }
}

"""
import serial
import sys
import time

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600)

    if ser.isOpen():
        print("Listening on: ", ser.portstr)
    else:
        sys.stderr.write('Failed to open serial on : %s\n' % ser.portstr)
        sys.exit(1)

    ser.write('r');
    ser.close();

if __name__ == '__main__':
    main()
