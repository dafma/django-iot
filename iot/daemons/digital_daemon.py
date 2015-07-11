# old news.  No more interacting directly with arduino anymore

from iot.models import *
from iot.libraries.gpiohelper import RPIDigitalPin
from iot.daemons.gpio_daemon import GPIODaemon

class DigitalDaemon(GPIODaemon):

	pin_controllers = {}

	def run(self):
		super(DigitalDaemon, self).run()
		while True:
			pass

	def setUp(self):
		super(DigitalDaemon, self).setUp()
		# todo: loop over config for pins, and set up pin controllers for each
		pin = 25
		pc = RPIDigitalPin(pin, self.high, self.low)
		pc.setup()
		self.pin_controllers[pin] = pc

	def high(self, channel):
		d = DeviceData(device=self.device, value=1)
		d.save()
		print `channel` + ' is high'

	def low(self, channel):
		d = DeviceData(device=self.device, value=0)
		d.save()
		print `channel` + ' is low'