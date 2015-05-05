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