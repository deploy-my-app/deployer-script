import requests

class ApiClient(object):
	"""docstring for ApiTokenValidator"""
	def __init__(self, url, conf):
		super(ApiTokenValidator, self).__init__()
		self.url= url #the url to the api /api/v1/tokens
		self.key=self.getKey()
		self.configManager=conf
		self.headers={"user-agent":"deployer-script-deamon/1.0.0","X-PUBLIC-KEY":""}
  #Authenticate the user with a basic http request
  def BasicHttpAuth(self):
    pass
  #Authenticate the user with the private key and user name given
  def KeyAuth(self):
  #authenticate the user
  def authenticate(self) :
    pass
  #This will create a key if the user doesnt already have one
  def createPublicKey(self):
    pass
  #this will create the private key
  def createPrivateKey(self):
    pass
  #this will read the config
	def getPublicKey(self):
    pass
  #this will read the config
  def getPrivateKey(self):
    pass
  #send a request against the api
  def sendRequest(self):
    pass
