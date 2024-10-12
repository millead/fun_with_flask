from flask import Flask

# Initialize the Flask application
app = Flask(__name__)

@app.route("/")
def hello_world():
  return "There is no anxiety in this and learning takes time - Power!"

# Run the flask server
if __name__ == "__main__":
    app.run()