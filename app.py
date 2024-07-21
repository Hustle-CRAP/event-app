from flask import Flask, request, render_template, redirect, url_for, flash, session
import mysql.connector
import bcrypt

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with your actual secret key

# Database connection
db = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="Admin@123",
    database="event_app_db"
)

cursor = db.cursor()

#

@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        print(request.form)
        username = request.form['loginEmail']
        password = request.form['loginPassword']

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            flash('Username already exists')
            return redirect(url_for('register'))

        # Hash the password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Store username and hashed password
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, password_hash))
        db.commit()
        flash('User registered successfully')
        return redirect(url_for('login'))

    return render_template('signin.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return request.form
        username = request.form['username']
        password = request.form['password']

        # Fetch the user's hashed password from the database
        cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()
        if not result:
            flash('Username not found')
            return redirect(url_for('login'))

        password_hash = result[0]

        # Check if the provided password matches the stored hashed password
        if bcrypt.checkpw(password.encode('utf-8'), password_hash.encode('utf-8')):
            session['username'] = username
            flash('Login successful')
            return redirect(url_for('home'))
        else:
            flash('Invalid password')
            return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
    
