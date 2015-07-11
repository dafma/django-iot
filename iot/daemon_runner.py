# ONLY keeping this for refrence atm.  Not going to need this anymore, but don't want to delete cause it was
# and interesting soln
from multiprocessing import Process
#from iot.daemons import * #nope
from iot.daemons.digital_daemon import DigitalDaemon
from iot.daemons.polling_daemon import PollingDaemon
from iot.models import Device, DeviceType
import pkgutil
import sys

def runAll():
	#this needs to work instead of including them like we are above
	devices = Device.objects.select_related('device_type').all()
	processes = []

	for d in devices:
		daemon = globals()[d.device_type.daemon_class](d)
		p = Process(target=daemon.run, args={})
		p.daemon = True
		p.start()
		processes.append(p)

	while True:
		for p in processes:
			p.join()


#this just doesn't work.  I need something that does
def load_all_modules_from_dir(dirname):
	for importer, package_name, _ in pkgutil.iter_modules([dirname]):
		full_package_name = '%s.%s' % (dirname, package_name)
		if full_package_name not in sys.modules:
			module = importer.find_module(package_name).load_module(full_package_name)
			print module
