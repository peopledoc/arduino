import serial
import time

from flask import Flask, redirect, request

app = Flask(__name__)
ser = serial.Serial('/dev/ttyACM0', 9600)
#ser.open()
if ser.isOpen():
    print("Listening on: ", ser.portstr)
else:
    sys.stderr.write('Failed to open serial on : %s\n' % ser.portstr)
    sys.exit(1)
    

def send_event(ser, led, total, on, off):
    """Write the data to the API.
    StartByte LedNumber TotalTime (seconds) OnTime(hundredth of second) OffTime(hundredth of second)
    """
    ser.flushInput()
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


@app.route("/", methods=['GET', 'POST'])
def hello():
    signal = request.form.get('signal')
    if signal:
        send_event(ser, 0, 40, 200, 0)
        send_event(ser, 1, 30, 200, 0)
        send_event(ser, 2, 20, 200, 0)
        send_event(ser, 3, 10, 200, 0)
        send_event(ser, 4, 50, 200, 0)
    return '<form method="post" action=""><input type="submit" name="signal" value="Send" /></form>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
