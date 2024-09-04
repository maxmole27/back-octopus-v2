import bcrypt


def hash_password(password: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password

def check_password(hashed_password: str, password: str):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password=hashed_password)