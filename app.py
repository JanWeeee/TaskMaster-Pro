from flask import Flask, render_template, redirect, url_for, request, session, flash
from api.routes import tasks_api
from api.models import init_db, db_session, User, Task
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)
app.register_blueprint(tasks_api, url_prefix='/api')
app.secret_key = os.urandom(24)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/tasks')
def tasks_page():
    if 'user_id' not in session:
        flash('Please log in to view your tasks.')
        return redirect(url_for('login_page'))

    user_id = session['user_id']
    user = db_session.query(User).get(user_id)
    tasks = db_session.query(Task).filter_by(user_id=user_id).all()
    return render_template('tasks.html', tasks=tasks, user=user)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db_session.query(User).filter_by(email=email).first()
        
        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('tasks_page'))
        else:
            flash('Invalid login credentials.')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register_page():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        existing_user = db_session.query(User).filter_by(email=email).first()
        if existing_user:
            flash('Email already registered. Please log in.')
            return redirect(url_for('login_page'))
        
        # Correct hash method
        hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
        new_user = User(username=username, email=email, password=hashed_password)
        db_session.add(new_user)
        db_session.commit()

        session['user_id'] = new_user.id
        return redirect(url_for('tasks_page'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You have been logged out.')
    return redirect(url_for('home'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
