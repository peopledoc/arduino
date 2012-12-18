# -*- coding: utf-8 -*-

""" Arduino services.
"""
from cornice import Service
import sys
import serial
import simplejson as json
from time import time

ser = serial.Serial('/dev/ttyACM1', 9600)
#ser.open()
if ser.isOpen():
    print "Listening on: ", ser.portstr
else:
    sys.stderr.write('Failed to open serial on : %s\n' % ser.portstr)
    sys.exit(1)

LEDS = range(5)
COLORS = ['blue', 'green', 'yellow', 'red', 'lamp']

next_led_event = [time()] * len(LEDS)
events = [[]] * len(LEDS)

arduino = Service(name='arduino', path='/',
                  description="Return the list of available leds")
led = Service(name='led', path='/led/{id}',
              description="Return the list of available leds")


class Event(object):
    def __init__(self, total, on, off):
        self.total = total / 100
        self.on = on / 10
        self.off = off / 10

    def send_event(self, led):
        """Write the data to the API.
        StartByte LedNumber TotalTime (deciseconds) OnTime(hundredth
        of second) OffTime(hundredth of second)
        """
        ser.flushInput()
        # Start byte
        ser.write('~')
        # Led id
        ser.write(chr(led))
        # Total time
        ser.write(chr(self.total))
        # On Time
        ser.write(chr(self.on))
        # Off Time
        ser.write(chr(self.off))


@arduino.get()
def get_info(request):
    """Returns Hello in JSON."""
    response = {led: COLORS[led] for led in LEDS}
    response['arduino'] = 'Bonjour'
    return  response


@led.post()
def post_event(request):
    led = request.matchdict['id']
    response = json.loads(request.body)
    kwargs = response.copy()
    event = Event(kwargs['total'], kwargs['on'],
                  kwargs['off'])
    event.send_event(int(led))
    response['arduino'] = 'Ok'
    return response


@arduino.post()
def post_sequence(request):
    sequence = json.loads(request.body)
    max_time = 0
    leds = []

    # On récupère le temps d'exec de notre sequence
    max_time = max([e['total'] for e in sequence['events']])

    # On récupère le timestamp à partir duquel toutes nos leds sont disponibles
    next_event = max([next_led_event[led] for led in [e['led'] for e in sequence['events']]])
    next_event_ok =  time() + 0.1

    if next_event < next_event_ok:
        next_event = next_event_ok

    for event in sequence['events']:
        led = int(event['led'])
        kwargs = event.copy()

        for key in kwargs.keys():
            if key not in ['total', 'on', 'off']:
                del kwargs[key]

        event_obj = Event(**kwargs)
        event_obj.send_event(led)
        # events[led].append({'time': next_event,
        #                     'event': Event(**kwargs)})
