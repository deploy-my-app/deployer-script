__author__ = "tricci"
__date__ = "$29 avr. 2015 15:51:47$"

def create_app():
	from server.routes import app
	
	return app