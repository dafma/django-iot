# old news
import time
from iot.daemons.gpio_daemon import GPIODaemon

class PollingDaemon(GPIODaemon):
	def run(self):
		super(PollingDaemon, self).run()
		while True:
			print self.device.name
			time.sleep(5)

	def setUp(self):
		super(PollingDaemon, self).setUp()
		# do more stuff