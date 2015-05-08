# All the routes for our application made minimal since we donnot need a whole tone of routes...normally

__author__ = "tricci"
__date__ = "$29 avr. 2015 15:51:57$"
from flask import abort
from flask import jsonify
from flask import make_response
from flask import request
from flask import Flask

app = Flask(__name__)
#Update the commands for a routine
@app.route("/routine/<routine_id>/commands",methods=["PUT"])
def update_commands(routine_id):
	pass
@app.route("/deploy/<deploy_id>/status",methods=["GET"])
def get_deploy_status(deploy_id):
	return jsonify({"id":deploy_id,"status":"the status"}),200
@app.route("/deploy",methods=["POST"])
def deploy():
	if request.args.get("deploy_id") and request.args.get("server_id") and request.args.get("routine_id") and request.args.get("command_id") :
		#run some commands here
		pass
	else:
		abort(501)
def unanimous(seq):
	try:
		it = iter(seq)
		first = it.next()
		return all(i == first for i in it)
	except StopIteration:
		return True

if __name__ == "__main__":
	app.run(debug=True,port=5000,host="0.0.0.0")
