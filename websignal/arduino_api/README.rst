Documentation
=============

USAGE
-----

Ping a led::

   curl -X POST http://127.0.0.1:6543/led/5 -d '{"total":1000, "on":100, "off":100}'

Send a sequence:

   curl -X POST http://127.0.0.1:6543/ -d '{"events":[{"led": 0, "total":10000, "on":200, "off":200}, {"led": 1, "total":10000, "on":100, "off":100}, {"led": 2, "total":10000, "on":200, "off":100}]}'
