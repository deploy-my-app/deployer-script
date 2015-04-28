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

class WebserverManager(Manager):#manage the web server
	"""docstring for WebserverManager"""
	def __init__(self, arg):
		super(WebserverManager, self).__init__()
		self.arg = arg
	def restart(self):
		pass
	
	def setHostname(self,name):
		pass
	def getHostname(self):
		pass
	def setDocumentRoot(self,path):
		pass
	def getDocumentRoot(self):
		pass
	def setPort(self,port):
		pass
	def getPort(self):
		pass
	
class MigrationManager(Manager):#migrate all databases (if available)
	"""docstring for MigrationManager"""
	def __init__(self, arg):
		super(MigrationManager, self).__init__()
		self.arg = arg
class CommandManager(Manager): #Manage scripts and system dependencies
	"""docstring for CommandManager"""
	def __init__(self, arg):
		super(CommandManager, self).__init__()
		self.arg = arg
	def getNodes(self):
		pass
class LogManager(Manager): # A manager to Log everything that is happening
	"""docstring for LogManager"""
	def __init__(self, arg):
		super(LogManager, self).__init__()
		self.arg = arg
class SystemManager(Manager):#manage system 
	"""docstring for SystemManager"""
	def __init__(self, arg):
		super(SystemManager, self).__init__()
		self.arg = arg
		
class ConfigManager(Manager):
	"""docstring for ConfigManager"""
	def __init__(self):
		super(ConfigManager, self).__init__()
		import json
		self.conf=json.loads(open(".conf").read())
		self.props=solf.conf
		self.set("public-key",open(".key").read())

		