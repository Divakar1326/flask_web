📧 Flask Email Signup App

A simple Flask web application that allows users to submit their email addresses, which are stored in a PostgreSQL database.

This project is great for learning how to:

Connect Flask with PostgreSQL

Work with environment variables securely

Deploy small web apps (Heroku, Render, Railway, etc.)

🚀 Features

🌐 Simple Flask web interface

🗄️ Stores user emails in a PostgreSQL database

🔒 Environment variables for secure DB connection

✅ Prevents duplicate emails using ON CONFLICT DO NOTHING

🎨 Minimal but modern UI with CSS styling

🛠️ Tech Stack

Backend: Flask

Database: PostgreSQL (via psycopg2)

Config: python-dotenv

Frontend: HTML + CSS (inline in Flask)

📂 Project Structure
📦 flask-email-signup
├── app.py              # Main Flask app
├── .env                # Environment variables (ignored in Git)
├── requirements.txt    # Dependencies
└── README.md           # Documentation

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/flask-email-signup.git
cd flask-email-signup

2️⃣ Create a virtual environment (optional)
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Setup environment variables

Create a .env file in the root folder:

DATABASE_URL=postgresql://username:password@hostname:port/dbname
PORT=10000


⚠️ Do not commit your .env file to GitHub.

5️⃣ Run the app
python app.py


Now open 👉 http://localhost:10000
