import os
import psycopg2
from flask import Flask, request, render_template_string
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

DB_URL = os.getenv("DATABASE_URL")

def get_db_connection():
    return psycopg2.connect(DB_URL, sslmode='require')

def create_table():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                email TEXT UNIQUE NOT NULL
            )
        """)
        conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")
        raise e
    finally:
        cur.close()
        conn.close()

try:
    create_table()
except Exception as e:
    print(f"Failed to initialize database: {e}")

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        email = request.form.get('email')
        if email:
            try:
                conn = get_db_connection()
                cur = conn.cursor()
                cur.execute("INSERT INTO users (email) VALUES (%s) ON CONFLICT DO NOTHING", (email,))
                conn.commit()
            except Exception as e:
                print(f"Error inserting email: {e}")
                return "Database error occurred", 500
            finally:
                cur.close()
                conn.close()
    
    return render_template_string("""
    <!-- Your HTML template remains the same -->
    """)

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
