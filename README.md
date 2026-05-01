# The Vault | Cybersecurity Lab & Educational Platform

A professional, hands-on cybersecurity lab built with Flask and SQLite to demonstrate two of the most critical vulnerabilities in modern web applications: **SQL Injection (SQLi)** and **Data Exposure** (Lack of Encryption).

## 🚀 Key Features

- **Vulnerable Login Lab**: A dedicated login page designed to be bypassed using common SQLi payloads.
- **Defense Toggles**: Real-time switches to toggle between "Vulnerable" (Raw SQL) and "Secure" (Parameterized Queries) modes.
- **AES-256 Encryption Engine**: A implementation of military-grade encryption to protect sensitive data at rest.
- **Interactive Dashboard**:
  - **Live Data Monitor**: See how data looks inside the database (Raw vs. Ciphertext).
  - **Attack Tutorial**: An integrated guide on how to perform and defend against SQLi.
  - **Password Strength Meter**: Real-time regex-based validation for secure passwords.
  - **Forensic Audit Log**: A timestamped trail of all security events and system actions.

## 🛠️ Tech Stack

- **Backend**: Python 3.x, Flask
- **Database**: SQLite3 (using both SQLAlchemy and Raw SQL for demonstration)
- **Security**: PyCryptodome (AES-256-CFB)
- **Frontend**: Bootstrap 5 (Light Professional Theme), FontAwesome 6, JavaScript

## 🧪 Educational Scenarios

### Scenario 1: The SQL Injection Breach
1. Navigate to the Login page.
2. Disable the **SQL Injection Patch**.
3. Use the payload: `admin' --` or `' OR '1'='1' --`.
4. Observe how the system grants access by commenting out the password check.

### Scenario 2: Data Exposure Observation
1. On the dashboard, disable **AES Encryption**.
2. Add a new user with a password.
3. Observe the "Vault Data Monitor" — the password and name are stored in plaintext (marked as **EXPOSED**).
4. Re-enable encryption and see the data immediately transform into unreadable ciphertext.

## ⚙️ Installation & Setup

1. **Clone the repository**:
   ```powershell
   git clone <repository-url>
   cd the-vault
   ```

2. **Install dependencies**:
   ```powershell
   pip install -r requirements.txt
   ```

3. **Initialize the Lab**:
   ```powershell
   python database_setup.py
   ```

4. **Run the Application**:
   ```powershell
   python app.py
   ```
   Open your browser to `http://127.0.0.1:5001`.

## ⚠️ Disclaimer
This project is for **educational purposes only**. It is designed to teach developers and students how to identify and prevent common web vulnerabilities. Never use these techniques on systems you do not have explicit permission to test.
