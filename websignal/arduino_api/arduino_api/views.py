""" Arduino services.
"""
from cornice import Service
import serial
import simplejson as json

ser = serial.Serial('/dev/ttyACM0', 9600)
#ser.open()
if ser.isOpen():
    print "Listening on: ", ser.portstr
else:
    sys.stderr.write('Failed to open serial on : %s\n' % ser.portstr)
    sys.exit(1)

LEDS = range(5)
COLORS = ['blue', 'green', 'yellow', 'red', 'lamp']

arduino = Service(name='arduino', path='/', description="Return the list of available leds")
led = Service(name='led', path='/led/{id}', description="Return the list of available leds")


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


@arduino.get()
def get_info(request):
    """Returns Hello in JSON."""
    response = {led : COLORS[led] for led in LEDS}
    response['arduino'] = 'Bonjour'
    return  response

@led.post()
def post_event(request):
    led = request.matchdict['id']
    response = json.loads(request.body)
    kwargs = response.copy()
    kwargs['total'] /= 100
    kwargs['on'] /= 10
    kwargs['off'] /= 10
    kwargs['led'] = int(led)
    send_event(ser, **kwargs)
    response['arduino'] = 'Ok'
    return response
