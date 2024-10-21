import hashlib

__user_input = input("Şifre girin: ")
pw = hashlib.sha256(__user_input.encode()).hexdigest()
print("Hashed password: ", pw)
encrypted_pw = ""

def encrtyp(password):


print("Encrypted password: ", encrtyp(pw, __user_input))
