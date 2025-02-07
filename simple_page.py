import os
from flask import Flask

# Initialize the Flask app
app = Flask(__name__)

# Define the home route
@app.route('/')
def hello_world():
    return """
    <html>
    <head>
        <style>
            body {
                background-image: url('https://example.com/your-image.jpg'); /* Replace with your image URL */
                background-size: cover;
                background-position: center;
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                color: white;
                font-family: Arial, sans-serif;
            }
            h1 {
                font-size: 4em;
                margin-bottom: 20px;
            }
            p {
                font-size: 2em;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Welcome to my first web page!</p>
    </body>
    </html>
    """

# Run the app
if __name__ == '__main__':
    # Get the PORT environment variable (default to 5000 if not set)
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
