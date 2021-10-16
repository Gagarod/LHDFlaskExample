#importing from flask package
import flask

#instantiating a flask website object that
#originates from __name__
app=flask.Flask(__name__)

#this is a routing decorator that sends the result
#of the function to our webapp
@app.route("/")

def main():
  return "Hello Blahaj?"


#https://stories.mlh.io/how-to-make-a-hack-planner-with-mongodb-8b6fa612645


#this function redirects user to google
@app.route("/google")
def google():
  return flask.redirect("https://google.com")
  
#this function redirects user to google
@app.route("/template")
def template():
  x=5
  return flask.render_template("template.html",x=x)  

@app.route("/variable/<var>")
def variable(var):
  return "The \"Secret\" variable is {}".format(var)

@app.route("/squalculator",methods=["GET","POST"])
def calculator():
  
  if flask.request.method=="GET":
    return flask.render_template("squalculator.html")
  if flask.request.method=="POST":
    value=flask.request.form["input"]
    if value=="":
      squared_value="na"
    else:
      try:
        squared_value=int(value)**2
      except ValueError:
        squared_value="error"
    return flask.render_template("squalculator.html",result=squared_value)  

app.run(host="0.0.0.0",port=5000,debug=True)  