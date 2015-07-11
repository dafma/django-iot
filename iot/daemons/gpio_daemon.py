# old news, no longer doing this
import json
from iot.libraries.gpiohelper import RPIDigitalPin
from iot.daemons.base_daemon import BaseDaemon

class GPIODaemon(BaseDaemon):
	'''Base daemon for controlling devices linked to GPIO pins on a RPI'''
	config = None

	def run(self):
		super(GPIODaemon, self).run()
		self.setUp()

	def setUp(self):
		self.config = json.loads(self.device.config)