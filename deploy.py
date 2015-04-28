#/usr/bin/env python3
"""
This script will deploy all cammands and pull the repository
"""

class CommandDeployer(object):
	"""docstring for CommandDeployer"""
	def __init__(self, apirul, key, user,logger):
		super(CommandDeployer, self).__init__()
		self.apirul = apiurl #url to get the commands
		self.key = key #the key for user to autheniticate
		self.user = user #the user to autheniticate
		self.logger=logger
		self.nodecount=
	def getCommands(self): #retrieve all the commands
		pass
	def authenticate(self): # authenitcate on the Api
		pass
	def deploy(self):#deploy everything
		for comm in self.getCommands():
			self.runCommand(comm)
	def runCommand(self,command): # run all the commands
		pass
	def waitOtherNodesFinish(self):
		pass
#deploys a git repo or a tar.gz download from the api
class RepoDeployer(object):
	"""docstring for CommandDeployer"""
	def __init__(self, apirul, giturl, key, user,logger,WebserverManager):
		super(CommandDeployer, self).__init__()
		self.apirul = apiurl #url to get the commands

		self.giturl = giturl
		self.key = key #the key for user to autheniticate
		self.user = user #the user to autheniticate
		self.logger=logger
		self.manager=WebserverManager

	def authenticate(self): # authenitcate on the Api
		pass
	def getRepo(self): #retrive the github url
		return str(self.giturl)
	def deploy(self):#deploy everything
		pass
	def cloneRepo(self): #clone the repo to the directory
		pass
#Deploys all envoronnement varaiibles
class EnvironementDeployer(object):
	"""docstring for EnvironementDeployer"""
	def __init__(self, arg):
		super(EnvironementDeployer, self).__init__()
		self.arg = arg
		