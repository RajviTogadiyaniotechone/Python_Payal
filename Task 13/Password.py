import random
import string

def generate_password(length=12):

    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Randomly select characters from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Generate a random password of specified length
password = generate_password(12)
print(f"Generated Password: {password}")
