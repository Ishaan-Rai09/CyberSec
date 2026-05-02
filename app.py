from flask import Flask, render_template, request, redirect, url_for, flash, session
from database_setup import db, ConfidentialUser, AuditLog, User
from security_engine import encrypt_data, decrypt_data
import os
import sqlite3

app = Flask(__name__)
app.secret_key = "flask-session-secret"
db_path = os.path.join(os.path.dirname(__file__), 'vault.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
db.init_app(app)

# SECURITY STATE: Toggle this to demonstrate attacks
SECURITY_SETTINGS = {
    "encryption_enabled": True,
    "authorization_checks": True,
    "audit_logging": True,
    "secure_login": False
}

def log_event(action, user_id=None, status="SUCCESS"):
    if SECURITY_SETTINGS["audit_logging"]:
        # Primary fix: Always seek the session username if user_id is missing
        actual_user = user_id or session.get('user_id') or "admin"
        
        new_log = AuditLog(action=action, user_identity=str(actual_user), status=status)
        db.session.add(new_log)
        db.session.commit()

@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    users = ConfidentialUser.query.all()
    logs = AuditLog.query.order_by(AuditLog.timestamp.desc()).limit(10).all()
    
    # Decrypt data for display ONLY if encryption is "handled" by current logic
    display_users = []
    for u in users:
        display_users.append({
            "id": u.id,
            "name": decrypt_data(u.name) if SECURITY_SETTINGS["encryption_enabled"] else u.name,
            "username": decrypt_data(u.username) if SECURITY_SETTINGS["encryption_enabled"] else u.username,
            "password": decrypt_data(u.password) if SECURITY_SETTINGS["encryption_enabled"] else u.password,
            "encrypted_name_demo": u.name # Keep raw version for side-by-side comparison
        })
    
    return render_template('index.html', 
                           users=display_users, 
                           logs=logs, 
                           security=SECURITY_SETTINGS,
                           logged_in=session.get('user_id'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if SECURITY_SETTINGS["secure_login"]:
            # SECURE: Using SQLAlchemy ORM (Parameterized)
            user = User.query.filter_by(username=username, password=password).first()
        else:
            # VULNERABLE: Direct string interpolation into Raw SQL
            # This allows ' OR '1'='1 handles
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            # USE COMMENT to ignore password check: ' OR '1'='1' --
            query = f"SELECT * FROM user WHERE username = '{username}' AND password = '{password}'"
            print(f"Executing Vulnerable Query: {query}")
            try:
                cursor.executescript(query) # executescript can handle multiple statements but we want results
                # Actually, standard execute is fine, but SQLi often needs to bypass the AND password part
                cursor.execute(query)
                user_row = cursor.fetchone()
            except Exception as e:
                print(f"SQL Error: {e}")
                user_row = None
            conn.close()
            
            # Map row to something we can use if found
            # sqlite3 fetchone returns a tuple. Table structure is likely (id, username, password)
            if user_row:
                user = {"username": user_row[1], "id": user_row[0]}
            else:
                user = None

        if user:
            session['user_id'] = user['username'] if isinstance(user, dict) else user.username
            flash(f"Logged in successfully as {session['user_id']}!")
            log_event(f"LOGIN: {session['user_id']}", user_id=session['user_id'])
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials.")
            log_event(f"FAILED_LOGIN: {username}", user_id=username, status="FAILURE")
            
    return render_template('login.html', security=SECURITY_SETTINGS)

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')

    if SECURITY_SETTINGS["encryption_enabled"]:
        new_user = ConfidentialUser(
            name=encrypt_data(name),
            username=encrypt_data(username),
            password=encrypt_data(password)
        )
    else:
        # VULNERABLE MODE: Store in plain text
        new_user = ConfidentialUser(name=name, username=username, password=password)
    
    db.session.add(new_user)
    db.session.commit()
    log_event(f"ADDED_USER: {username}", user_id=session.get('user_id'))
    return redirect(url_for('index'))

@app.route('/toggle_security/<feature>')
def toggle_security(feature):
    if feature in SECURITY_SETTINGS:
        SECURITY_SETTINGS[feature] = not SECURITY_SETTINGS[feature]
        log_event(f"SECURITY_TOGGLE: {feature} to {SECURITY_SETTINGS[feature]}", user_id=session.get('user_id'))
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Seed a test user if none exists
        if not User.query.filter_by(username='admin').first():
            admin = User(username='admin', password='securepassword123')
            db.session.add(admin)
            db.session.commit()
            print("Seeded admin user.")
    app.run(debug=True, port=5001)
