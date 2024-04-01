from flask import Flask, render_template

# Initialize the Flask application
app = Flask(__name__)

# Define the routes
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

# Check if the app.py file is being run directly and not imported
if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
