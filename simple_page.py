import os
import psycopg2
from flask import Flask, request, render_template_string

# Initialize the Flask app
app = Flask(__name__)

# Database connection details
DB_URL = os.getenv("DATABASE_URL")  # Render provides this environment variable

# Create table if not exists
def create_table():
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email TEXT UNIQUE NOT NULL
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

create_table()

# Define the home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            conn = psycopg2.connect(DB_URL, sslmode="require")
            cur = conn.cursor()
            cur.execute("INSERT INTO users (email) VALUES (%s) ON CONFLICT DO NOTHING", (email,))
            conn.commit()
            cur.close()
            conn.close()
    
    return render_template_string("""
    <html>
    <head>
        <style>
            body {
                background-image: url("/static/bg.jpg"); /* Replace with your image URL */
                background-size: cover;
                background-position: center;
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                text-align: center;
                color: white;
                font-family: Arial, sans-serif
            }
            h1 {
                font-size: 4em;
            }
            p {
                font-size: 2em;
            }
            form {
                margin-top: 20px;
            }
            input[type="email"] {
                padding: 10px;
                font-size: 1.2em;
            }
            button {
                padding: 10px;
                font-size: 1.2em;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>Hello, World!</h1>
        <p>Welcome to my first web page!</p>
        <form method="POST">
            <input type="email" name="email" placeholder="Enter your email" required>
            <button type="submit">Submit</button>
        </form>
    </body>
    </html>
    """)

# Run the app
if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
