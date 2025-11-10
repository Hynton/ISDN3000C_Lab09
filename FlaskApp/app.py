import sqlite3
# Add request, url_for, and redirect to imports
from flask import Flask, render_template, request, url_for, redirect, jsonify, flash

# Create the Flask app and point to the templates folder
app = Flask(__name__, template_folder='templates')
# Secret key is required for flashing (session). Change this for production.
app.config['SECRET_KEY'] = 'dev-secret-change-me'


# Function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row  # This allows us to access columns by name
    return conn


@app.route('/api/messages', methods=['POST'])
def add_message_api():
    data = request.get_json()
    name = data.get('name')
    message = data.get('message')

    if not name or not message:
        return jsonify({'status': 'error', 'message': 'Name and message are required.'}), 400

    conn = get_db_connection()
    conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)',
                 (name, message))
    conn.commit()
    conn.close()

    return jsonify({'status': 'success', 'message': 'Message added!'})


# Coding 3
@app.route('/', methods=('GET', 'POST'))
def index():
    conn = get_db_connection()

    if request.method == 'POST':
        name = request.form.get('name', '').strip()
        message = request.form.get('message', '').strip()

        # Length validation
        if len(message) > 140:
            flash('Message is too long (maximum 140 characters).', 'error')
            conn.close()
            return redirect(url_for('index'))

        # Insert the message
        conn.execute('INSERT INTO messages (name, message) VALUES (?, ?)',
                     (name, message))
        conn.commit()
        conn.close()
        # Redirect to prevent form resubmission
        flash('Message posted.', 'success')
        return redirect(url_for('index'))

    # This code runs for a GET request
    messages = conn.execute(
        'SELECT * FROM messages ORDER BY created_at DESC').fetchall()
    conn.close()

    return render_template(
        'index.html',
        page_title='Guestbook Home',
        messages=messages
    )


# Coding 2
"""
@app.route('/')
def index():
    # A dummy list of messages for now
    movie_name = ["The Last Emperor", "The Pianist", "JoJo Rabbit"]

    # Pass variables to the template
    return render_template(
        'index.html',
        page_title='Movie Home',
        messages=movie_name
    )
"""


# A simple health check route
@app.route('/health')
def health_check():
    return 'Server is running!', 200


# Coding 1
"""
@app.route('/about')
def about_page():
    return 'This is a simple Flask guestbook application.', 200
"""
