class ConfigManager(Manager):
	"""docstring for ConfigManager"""
	def __init__(self):
		super(ConfigManager, self).__init__()
		import json
		self.conf=json.loads(open(".conf").read())
		self.props=solf.conf
		self.set("public-key",open(".key").read())