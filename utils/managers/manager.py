"""
This script will contain all managers for the services, such as the rebooting, changing nginx/apache configuration, deploy
"""
class Manager(object):
	"""docstring for Manager"""
	def __init__(self, arg):
		super(Manager, self).__init__()
		self.arg = arg
	def get(self,key):
		try:
			return self.props[key]
		except KeyError:
			return None
	def set(self,key,value):
		if key in self.props:
			return False
		else:
			self.props[key]=value
			return True
		


		