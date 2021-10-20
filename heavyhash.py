import bcrypt
import scrypt

password=input('Type in a password: ').encode("utf-8")

salt=bcrypt.gensalt().encode("utf-8")
hashed_b=bcrypt.hashpw(password,salt)
hashed_s=scrypt.hash(password,salt)

print('   Password:',password.decode("utf-8"))
print('       Salt:',salt.decode("utf-8"))
print('Bcrypt Hash:',hashed_b)
print('Scrypt Hash:',hashed_s.hex())

# bcrypt.checkpw()
'''
Compares the user input with the stored, hashed password to
see if they are the same.

Args:
plain text password
hashed password

Returns:
True
False
'''
