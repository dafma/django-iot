import time
# from models import *

class BaseDaemon(object):
	"""Base Daemon object"""

	# holds arguments to run daemon with
	args = {}
	name = False	

	def __init__(self, args={}):
		self.args = args
		if args['name']:
			self.name = args['name']
		else:
			self.name = 'unnamed' 		

	def run(self, args={}):
		while True:
			print self.name
			time.sleep(5)

	def setArgs(self, args={}):
		self.args = args

	def getArgs(self):
		return self.args

class SensorLoggerDaemon(BaseDaemon):
	"""Base Sensor Logger object"""

	sensor = False
	state = False
	name = False
	frequency = False

	def __init__(self, args={}):
		super(SensorLoggerDaemon, self).__init__(args)
		if args['sensor_id']:
			self.setSensor(args['sensor_id'])
		else:
			raise Exception('Must specify a sensor_id')

		if args['frequency']:
			self.setFrequency(args['frequency'])
		else:
			self.setFrequency(60)

		if args['name']:
			self.name = args['name']		
		
	
	def start(self):
		if not(self.state):			
			#start running
			super(SensorLoggerDaemon, self).start()
			self.state = True
			self.log()

	def stop(self):
		if self.state:
			#stop running
			super(SensorLoggerDaemon, self).stop()	
			self.state = False

	def setSensor(self, sensor_id):
		self.sensor = sensor_id

	def getSensor(self):
		return self.sensor

	def setFrequency(self, frequency):
		self.frequency = frequency

	def getFrequency(self):
		return self.frequency

	def run(self):
		while self.state:
			self.poll()
			time.sleep(self.frequency)

	def poll(self):
		print self.name + ' Polled'