class BaseDaemon(object):
	"""Base Daemon object"""

	# holds arguments to run daemon with
	device = None

	def __init__(self, device):
		self.device = device

	def run(self):
		'''Override to provide daemon functionality'''
		pass