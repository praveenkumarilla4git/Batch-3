# Import the Flask class from the flask library we just installed
from flask import Flask

# Create an instance of the Flask class.
# __name__ helps Flask know where to look for resources (like files/templates).
app = Flask(__name__)

# This is a "Decorator". It links the URL path '/' (the homepage) to the function below.
# So, when you go to http://localhost:5000/, this triggers.
@app.route('/')
def hello():
    # This function returns HTML text to the browser.
    # The browser reads <h1> and makes the text big and bold.
    return "<h1>Hello! This is running locally on Windows!</h1>"

# This line checks if this script is being executed directly (not imported).
if __name__ == "__main__":
    # Start the web server!
    # port=5000 is the specific "door" the server listens on.
    app.run(port=5000)