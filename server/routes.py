# All the routes for our application made minimal since we donnot need a whole tone of routes...normally

__author__ = "tricci"
__date__ = "$29 avr. 2015 15:51:57$"

@app.route("/deploy",methods=["POST"])
def deploy():
  #request.json["deployement"]
  #The deploy conaints some thing like a deployement in the database exept it doesnt have the statuses
  pass


if __name__ == "__main__":
  print "Hello World"
