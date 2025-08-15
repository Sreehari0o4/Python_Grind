# Password Manager (Learning)

Minimal terminal password manager that stores usernames and encrypted passwords using Fernet (symmetric encryption). For learning only—do not use for real credentials.

## Contents
- passwrd_manager.py — CLI to add/view passwords
- passwords.txt — encrypted entries (created at runtime)
- key.key — encryption key (must exist; keep it safe)

## Setup

Requirements:
- Python 3.10+
- cryptography

Windows (PowerShell):
```powershell
cd C:\zreehari\python\learn\password_manager
python -m pip install cryptography
# Create the encryption key (run once in this folder):
python -c "from cryptography.fernet import Fernet; open('key.key','wb').write(Fernet.generate_key())"
# Run
python .\passwrd_manager.py
```

## Usage
- add — add a username and password (stored encrypted in passwords.txt)
- view — list saved entries (decrypted using key.key)
- q — quit

Notes:
- Do not lose key.key; without it, passwords cannot be decrypted.
- Keep key.key private and secure.