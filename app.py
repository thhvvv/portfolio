from flask import Flask, render_template
from routes import main
from config import Config
from models import db

app = Flask(__name__)

app.config.from_object(Config)

# Initialize the database
db.init_app(app)

# Register blueprints
app.register_blueprint(main)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('service.html')

@app.route('/feature')
def feature():
    return render_template('feature.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Optional for handling 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
