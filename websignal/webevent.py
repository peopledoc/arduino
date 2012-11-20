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
    
@app.route("/", methods=['GET', 'POST'])
def hello():
    signal = request.form.get('signal')
    if signal:
        if ser.isOpen():
            ser.write('H');
            time.sleep(2);
            ser.write('L');
            time.sleep(2);
            return redirect('/')
        else:
            return 'Serial %s was closed.\n'            
        
    return '<form method="post" action=""><input type="submit" name="signal" value="Send" /></form>'

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
