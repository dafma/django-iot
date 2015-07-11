from daemons import *

#holds references to all our daemon objects
daemons = {}

#Here we instantiate individual daemons that should run
daemons['PlantHumidity'] = SensorLoggerDaemon({'sensor_id': 1, 'frequency': 60, 'name': 'Plant1Humidity'})
daemons['Sunlight'] = SensorLoggerDaemon({'sensor_id': 2, 'frequency': 60, 'name': 'Sunlight'})
daemons['Temp'] = SensorLoggerDaemon({'sensor_id': 3, 'frequency': 60, 'name': 'Temp'})