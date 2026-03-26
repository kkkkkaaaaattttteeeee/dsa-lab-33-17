from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

# Инициализация приложения
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret-key-for-lab5'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Инициализация базы данных и менеджера логина
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Модель пользователя
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    name = db.Column(db.String(100), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Создание таблиц
with app.app_context():
    db.create_all()

# Корневая страница
@app.route('/')
def index():
    if current_user.is_authenticated:
        return render_template('index.html', user=current_user)
    return redirect(url_for('login'))

# Страница входа (GET)
@app.route('/login', methods=['GET'])
def login_page():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('login.html')

# Обработка входа (POST)
@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    
    user = User.query.filter_by(email=email).first()
    
    if not user:
        flash('Пользователь не найден', 'error')
        return render_template('login.html')
    
    if not check_password_hash(user.password, password):
        flash('Неверный пароль', 'error')
        return render_template('login.html')
    
    login_user(user)
    return redirect(url_for('index'))

# Страница регистрации (GET)
@app.route('/signup', methods=['GET'])
def signup_page():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('signup.html')

# Обработка регистрации (POST)
@app.route('/signup', methods=['POST'])
def signup():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    
    existing_user = User.query.filter_by(email=email).first()
    
    if existing_user:
        flash('Пользователь с таким email уже существует', 'error')
        return render_template('signup.html')
    
    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password=hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    flash('Регистрация успешна! Войдите в систему', 'success')
    return redirect(url_for('login_page'))

# Выход
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login_page'))

if __name__ == '__main__':
    app.run(debug=True)