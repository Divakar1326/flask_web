import os
import psycopg2
from flask import Flask, request, render_template_string
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

DB_URL = os.getenv("DATABASE_URL")
print(f"Using Database URL: {DB_URL}")  # Temporary debug line

def get_db_connection():
    try:
        return psycopg2.connect(DB_URL, sslmode='require')
    except Exception as e:
        print(f"Connection error: {e}")
        return None

def create_table():
    conn = None
    try:
        conn = get_db_connection()
        if conn:
            cur = conn.cursor()
            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    email TEXT UNIQUE NOT NULL
                )
            """)
            conn.commit()
            cur.close()
    except Exception as e:
        print(f"Error creating table: {e}")
    finally:
        if conn:
            conn.close()

@app.route('/', methods=['GET', 'POST'])
def home():
    message = ""
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            try:
                conn = get_db_connection()
                if conn:
                    cur = conn.cursor()
                    cur.execute("INSERT INTO users (email) VALUES (%s) ON CONFLICT DO NOTHING", (email,))
                    conn.commit()
                    cur.close()
                    conn.close()
                    message = "Email saved successfully!"
            except Exception as e:
                print(f"Error saving email: {e}")
                message = "Error saving email"
    
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Email Signup</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                display: flex;
                flex-direction: column;
                align-items: center;
                min-height: 100vh;
                background-color: #f0f2f5;
            }
            .container {
                background-color: white;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                width: 100%;
                max-width: 500px;
                margin-top: 40px;
            }
            h1 {
                color: #1a73e8;
                margin-bottom: 20px;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 15px;
            }
            input[type="email"] {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 16px;
            }
            button {
                padding: 10px;
                background-color: #1a73e8;
                color: white;
                border: none;
                border-radius: 4px;
                cursor: pointer;
                font-size: 16px;
            }
            button:hover {
                background-color: #1557b0;
            }
            .message {
                color: {% if 'Error' in message %}red{% else %}green{% endif %};
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome!</h1>
            <form method="POST">
                <input type="email" name="email" placeholder="Enter your email" required>
                <button type="submit">Submit</button>
            </form>
            {% if message %}
            <p class="message">{{ message }}</p>
            {% endif %}
        </div>
    </body>
    </html>
    """, message=message)

if __name__ == '__main__':
    create_table()
    port = int(os.getenv("PORT", 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
