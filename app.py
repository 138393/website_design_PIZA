from flask import Flask 

app = Flask(__name__)
#print("hello, world")
@app.route("/")  # this means whenever root gets called then print hello_world

def hello_world():
  return "hello, new user"


if __name__ == "__main__":
  app.run(host = '0.0.0.0')