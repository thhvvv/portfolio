from flask import Flask, render_template, flash, redirect, url_for
from users.routes import main
from config import Config
from users.forms import csrf
from models.models import db, User
from flask_login import LoginManager, login_required, current_user, login_user
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
csrf.init_app(app)
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
    return render_template('services.html')

@app.route('/feature')
def feature():
    return render_template('feature.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about_us')
def about_us():
    return render_template('about.html')

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)

# Define the user loader callback for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    # Load and return the user object by its ID
    return User.query.get(int(user_id))

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            if user.role == 'farmer':
                return redirect(url_for('farmer_dashboard'))
            elif user.role == 'company':
                return redirect(url_for('company_dashboard'))
            elif user.role == 'agrishop':
                return redirect(url_for('agrishop_dashboard'))
        else:
            flash('Invalid credentials, please try again')
    return render_template('login.html', form=form)

@app.route('/farmer_dashboard')
@login_required
def farmer_dashboard():
    return render_template('farmer_dashboard.html')

@app.route('/company_dashboard')
@login_required
def company_dashboard():
    return render_template('company_dashboard.html')

@app.route('/agrishop_dashboard')
@login_required
def agrishop_dashboard():
    return render_template('agrishop_dashboard.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the username already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already exists. Please choose a different one.', 'error')
            return redirect(url_for('register'))

        # Create a new user
        new_user = User(username=username)
        new_user.set_password(password)  # Hash and set the password

        try:
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful! Please log in.', 'success')
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash('There was an error in registration. Please try again.', 'error')

    return render_template('register.html')

# Optional for handling 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
