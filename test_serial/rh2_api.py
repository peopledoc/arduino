import serial
import sys
import time

def send_event(ser, led, total, on, off):    
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
    try:
        ser.open()
    except:
        print "Serial already open."

    if ser.isOpen():
        print("Listening on: ", ser.portstr)
    else:
        sys.stderr.write('Failed to open serial on : %s\n' % ser.portstr)
        sys.exit(1)

    send_event(ser, 0, 0, 50, 50)
    send_event(ser, 1, 0, 30, 30)
    send_event(ser, 2, 0, 20, 20)
    send_event(ser, 3, 0, 10, 10)
    
    ser.close();

if __name__ == '__main__':
    main()
