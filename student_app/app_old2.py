# app.py (Final DB Connection Test - LOCAL WINDOWS MACHINE)
from flask import Flask
import mysql.connector

app = Flask(__name__)

# --- CONFIGURATION (CRUCIAL: UPDATE HOST) ---
DB_CONFIG = {
    'host': '44.221.85.47',  # <--- REPLACE THIS IP!
    'user': 'admin',
    'password': 'database@1',
    'database': 'school_db',
    'port': 3306
}

def get_db_connection():
    """Tries to establish a MySQL database connection and handles errors."""
    try:
        conn = mysql.connector.connect(**DB_CONFIG)
        if conn.is_connected():
            return conn
        else:
            return None
    except mysql.connector.Error as err:
        # This will print the error in the VS Code terminal if it fails
        print(f"Database Connection Error: {err}") 
        return None

@app.route('/')
def test_db_connection():
    conn = get_db_connection()
    if conn:
        conn.close()
        return '<h1>✅ Database Connection SUCCESS!</h1>'
    else:
        return '<h1>❌ Database Connection FAILED! Check console errors and EC2 Security Group.</h1>', 500

if __name__ == '__main__':
    app.run(debug=True)