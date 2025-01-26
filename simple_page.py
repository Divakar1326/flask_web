from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def hello_world():
    return "<h1>Hello, World!</h1><p>Welcome to my first web page!</p>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
