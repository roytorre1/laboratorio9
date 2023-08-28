# generar contraseña

import random
import string

def generate_random_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars):
    try:
        if length <= 0:
            raise ValueError("La longitud debe ser un número positivo.")

        allowed_chars = ""
        if use_uppercase:
            allowed_chars += string.ascii_uppercase
        if use_lowercase:
            allowed_chars += string.ascii_lowercase
        if use_numbers:
            allowed_chars += string.digits
        if use_special_chars:
            allowed_chars += string.punctuation

        if not allowed_chars:
            raise ValueError("Debes seleccionar al menos un tipo de caracter.")

        random_char = lambda: random.choice(allowed_chars)
        password = ''.join(random_char() for _ in range(length))

        return password

    except ValueError as ve:
        return f"Error: {ve}"

# la cantidad de caracteres podemos eligir a nuestro gusto
length = 12
use_uppercase = True
use_lowercase = True
use_numbers = True
use_special_chars = True

password = generate_random_password(length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
print("Contraseña generada:", password)