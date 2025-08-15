# Password Manager (Learning)

Minimal terminal password manager that stores usernames and encrypted passwords using Fernet. For learning only—do not use real credentials.

## Contents
- passwrd_manager.py — CLI to add/view passwords
- passwords.txt — encrypted entries (created at runtime)
- key.key — encryption key (must exist in this folder)

## Setup
Requirements: Python 3.10+, cryptography

Install dependency (Windows PowerShell):
```powershell
python -m pip install cryptography
```

Generate the encryption key (one-time, creates key.key in this folder):
- Windows (PowerShell):
```powershell
python -c "from cryptography.fernet import Fernet; open('key.key','wb').write(Fernet.generate_key())"
```
- Ubuntu/macOS (bash):
```bash
python3 - <<'PY'
from cryptography.fernet import Fernet
open('key.key','wb').write(Fernet.generate_key())
print('key.key created')
PY
```
Alternative: uncomment write_key() in passwrd_manager.py and run once.

Run:
```powershell
python .\passwrd_manager.py
```

## Usage
- add — add a username and password
- view — list saved entries
- q — quit

Notes:
- Do not lose key.key; without it, entries cannot be decrypted.
- Keep key.key private; do not commit key.key or