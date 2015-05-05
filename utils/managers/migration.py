class MigrationManager(Manager):#migrate all databases (if available)
	"""docstring for MigrationManager"""
	def __init__(self, arg):
		super(MigrationManager, self).__init__()
		self.arg = arg