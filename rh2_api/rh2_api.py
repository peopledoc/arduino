import serial
import sys
import time

def send_event(ser, led, total, on, off):
    """Write the data to the API.
    StartByte LedNumber TotalTime (seconds) OnTime(hundredth of second) OffTime(hundredth of second)
    """
    # Start byte
    ser.write('~')
    # Led id
    ser.write(chr(led))
    # Total time
    ser.write(chr(total))
    # On Time
    ser.write(chr(on))
    # Off Time
    ser.write(chr(off))    

def main():
    ser = serial.Serial('/dev/ttyACM1', 9600)
    time.sleep(3) # Time to let the arduino start.
    print "Run"
    try:
        ser.open()
    except:
        print "Serial already open."

    if ser.isOpen():
        print("Listening on: ", ser.portstr)
    else:
        sys.stderr.write('Failed to open serial on : %s\n' % ser.portstr)
        sys.exit(1)

    while True:
        send_event(ser, 0, 250, 120, 120)
        send_event(ser, 1, 250, 60, 60)
        send_event(ser, 2, 250, 30, 30)
        send_event(ser, 3, 250, 15, 15)
        time.sleep(26)
    
    ser.close();

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print
