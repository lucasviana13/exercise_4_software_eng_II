import re

def is_secure_password(password: str) -> bool:
    if not isinstance(password, str):
        raise ValueError("A entrada deve ser uma string")
    if len(password) < 8:
        return False
    if not re.search(r"[0-9]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[!@#$%^&*()\-_=+<>?~]", password):
        return False
    return True
