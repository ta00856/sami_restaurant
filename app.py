from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
import psycopg2
import psycopg2.extras
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config





# Initialize the Flask application
app = Flask(__name__)
app.config.from_object(Config)

secret_key = app.config['SECRET_KEY']

while True:
    try:
        conn = psycopg2.connect(host='localhost', database='uncle_sami', user = 'postgres',password = 'Kzzs@022704')
        cursor = conn.cursor()
        print("Database connection succesful")
        break
    except Exception as error :
        print("Database connection failed")
        print("Error", error)
  
       

        
        
        
@app.route('/')
def home():
    # Render the home page template
    
    return render_template('index.html')

@app.route('/menu')
def menu():
    # Render the menu page template
    return render_template('menu.html')

@app.route('/restaurants')
def restaurants():
    # Render the restaurants page template
    return render_template('restaurants.html')

@app.route('/our-story')
def our_story():
    # Render the our story page template
    return render_template('our_story.html')

@app.route('/delivery')
def delivery():
    # Render the delivery page template
    return render_template('delivery.html')

@app.route('/soul-powered')
def soul_powered():
    # Render the soul powered page template
    return render_template('soul_powered.html')

@app.route('/join-us')
def join_us():
    # Render the join us page template
    return render_template('join_us.html')

@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')

    # Check if name, email, and password are provided
    if not name or not email or not password:
        flash('Name, email, and password are required')
        return redirect(url_for('home'))

    hashed_password = generate_password_hash(password)

    try:
        cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        
        cur.execute('SELECT * FROM users WHERE email = %s', (email,))
        user = cur.fetchone()
        if user:
            flash('Email already exists')
            return redirect(url_for('home'))
        
        print("Inserting user:", name, email, hashed_password)
        cur.execute('INSERT INTO users (name, email, password_hash) VALUES (%s, %s, %s)',
                    (name, email, hashed_password))
        conn.commit()
        cur.close()
        flash('Signup successful')
        print("User inserted successfully")
    except psycopg2.Error as e:
        flash('Error occurred while signing up: {}'.format(e))
        print("Database error:", e)
    finally:
        if cur is not None:
            cur.close()
    flash('Signup successful', 'success') 
    return redirect(url_for('home'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        try:
            cursor = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
            user = cursor.fetchone()
            if user and check_password_hash(user['password_hash'], password):
                session['email'] = email
                # flash('Login successful', 'success')
                # Render a template that includes a JavaScript redirect
                return render_template('login_success.html', redirect_url=url_for('home'))
            else:
                flash('Invalid email or password', 'danger')
        except psycopg2.Error as e:
            flash(f'Error occurred while logging in: {e}', 'danger')
            print("Database error:", e)
        finally:
            cursor.close()

    return render_template('login.html')


# Other routes and functionalities remain the same

# Check if the app.py file is being run directly and not imported


# Check if the app.py file is being run directly and not imported
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)