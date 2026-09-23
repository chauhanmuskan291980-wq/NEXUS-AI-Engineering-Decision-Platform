from pwdlib import PasswordHash
Password_hash = PasswordHash.recommended()

def hash_password(password:str) -> str:
    return Password_hash.hash(password)

def verify_password(
        plain_password:str,
        hashed_password:str,
)->bool:
    return Password_hash.verify(
        plain_password,
        hashed_password
    )