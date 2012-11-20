"""Make a serial led.

// Code on the arduino

int led = 13;
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
"""
import serial
import sys
import time

def main():
    ser = serial.Serial('/dev/ttyACM0', 9600)
    #ser.open()
    if ser.isOpen():
        print("Listening on: ", ser.portstr)
    else:
        sys.stderr.write('Failed to open serial on : %s\n' % ser.portstr)
        sys.exit(1)
    
    while ser.isOpen():
        ser.write('H');
        time.sleep(2);
        ser.write('L');
        time.sleep(2);

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print "\nBye bye"
