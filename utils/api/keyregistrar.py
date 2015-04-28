import requests
class KeyRegistrar(object):
	"""docstring for ApiTokenValidator"""
	def __init__(self, url, ConfigManager):
		super(ApiTokenValidator, self).__init__()
		self.url= url #the url to the api /api/v1/tokens
		self.key=self.getKey()
		self.configManager=ConfigManager
		self.headers={"user-agent":"deployer-script-deamon/1.0.0","X-PUBLIC-KEY"}
	def validate(self,key):
		

		req=requests.post(self.url,headers=self.headers)
		if req.status_code == "401":
			return False
		elif req.status_code == "403":
			return False
		elif req.status_code == "200":
			return True
	def getKey(self):
		return self.configManager.get('public-key')
