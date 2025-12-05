# app.py (Full Application Logic - Final Version for Test)

from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

# --- CONFIGURATION ---

app = Flask(__name__)
app.secret_key = 'supersecretkey' 

# Database config - USING YOUR EC2 PUBLIC IP!
DB_CONFIG = {
    'host': '44.221.85.47', # <--- YOUR EC2 IP
    'user': 'admin',
    'password': 'database@1',
    'database': 'school_db',
    'port': 3306
}

# Simple in-memory user store for demonstration
USERS = {
    'admin@school.com': {'password': 'adminpass', 'role': 'admin'},
    'teacher@school.com': {'password': 'teachpass', 'role': 'teacher'},
    'student@school.com': {'password': 'studpass', 'role': 'student'}
}

# --- DATABASE CONNECTION UTILITY ---

def get_db_connection():
    """Establishes and returns a MySQL database connection."""
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as err:
        print(f"Error connecting to MySQL: {err}")
        return None

# --- AUTHENTICATION ROUTES ---

@app.route('/')
def index():
    """Home page - redirects to dashboard if logged in."""
    if 'user_role' in session:
        return redirect(url_for(f'{session["user_role"]}_dashboard'))
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """Dummy sign-up view."""
    if request.method == 'POST':
        flash('Sign up successful! Please log in (using one of the 3 pre-defined users).', 'success')
        return redirect(url_for('login'))
    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login view."""
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = USERS.get(email)
        
        if user and user['password'] == password:
            session['logged_in'] = True
            session['username'] = email
            session['user_role'] = user['role']
            flash(f'Logged in successfully as {user["role"].upper()}.', 'success')
            return redirect(url_for(f'{user["role"]}_dashboard'))
        else:
            flash('Invalid credentials. Please try again.', 'error')
            
    return render_template('login.html')

@app.route('/logout')
def logout():
    """Logout view."""
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('user_role', None)
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

# --- ROLE-SPECIFIC DASHBOARDS AND FUNCTIONALITY ---

@app.route('/teacher_dashboard', methods=['GET', 'POST'])
def teacher_dashboard():
    """Teacher dashboard: Data entry for student details."""
    if session.get('user_role') != 'teacher':
        flash('Access denied. Teacher login required.', 'error')
        return redirect(url_for('login'))

    if request.method == 'POST':
        school_name = request.form['school_name']
        school_branch = request.form['school_branch']
        student_name = request.form['student_name']
        student_roll = request.form['student_roll']
        
        conn = get_db_connection()
        if conn:
            try:
                cur = conn.cursor()
                # Inserts the student data collected from the form
                sql = "INSERT INTO student_basic (school_name, school_branch, student_name, student_roll) VALUES (%s, %s, %s, %s)"
                cur.execute(sql, (school_name, school_branch, student_name, student_roll))
                conn.commit()
                flash("Student details saved successfully into EC2 MySQL!", 'success')
            except mysql.connector.Error as err:
                flash(f"Database Error: Could not save details. {err}", 'error')
            finally:
                if conn and conn.is_connected():
                    cur.close()
                    conn.close()
        else:
            flash("Could not connect to the database.", 'error')
        
        return redirect(url_for('teacher_dashboard'))

    return render_template('teacher_dashboard.html')

@app.route('/student_dashboard')
def student_dashboard():
    """Student dashboard."""
    if session.get('user_role') != 'student':
        flash('Access denied. Student login required.', 'error')
        return redirect(url_for('login'))
    return render_template('student_dashboard.html')

@app.route('/admin_dashboard')
def admin_dashboard():
    """Admin dashboard."""
    if session.get('user_role') != 'admin':
        flash('Access denied. Admin login required.', 'error')
        return redirect(url_for('login'))
    return render_template('admin_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)