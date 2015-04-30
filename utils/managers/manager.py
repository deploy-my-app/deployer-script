class Manager(object): #main manager
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
		


		