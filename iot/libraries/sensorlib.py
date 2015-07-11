# No longer used
from iot.models import *

class SensorLogger():
	"""Base Sensor Logger object"""

	sensor = False

	def __init__(self, sensor_id):
		self.setSensor(sensor_id)
		
	def log(self, data_point):
		return SensorData.objects.create(value=data_point, sensor=self.sensor)

	def setSensor(self, sensor_id):
		self.sensor = Sensor.objects.get(id=sensor_id)

	def getSensor(self):
		return self.sensor
