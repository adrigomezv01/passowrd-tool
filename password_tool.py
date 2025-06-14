import random
import string

def generar_contraseña(longitud=12, mayusculas=True, minusculas=True, numeros=True, simbolos=True):
    caracteres = ''
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        raise ValueError("¡Debes seleccionar al menos un tipo de carácter!")

    return ''.join(random.choice(caracteres) for _ in range(longitud))

def auditar_contraseña(contraseña):
    longitud = len(contraseña)
    mayusculas = any(c.isupper() for c in contraseña)
    minusculas = any(c.islower() for c in contraseña)
    numeros = any(c.isdigit() for c in contraseña)
    simbolos = any(c in string.punctuation for c in contraseña)

    score = sum([mayusculas, minusculas, numeros, simbolos])

    print(f"Longitud: {longitud}")
    print(f"Contiene mayúsculas: {mayusculas}")
    print(f"Contiene minúsculas: {minusculas}")
    print(f"Contiene números: {numeros}")
    print(f"Contiene símbolos: {simbolos}")

    if longitud >= 12 and score == 4:
        print("Nivel de seguridad: ALTO")
    elif longitud >= 8 and score >= 3:
        print("Nivel de seguridad: MEDIO")
    else:
        print("Nivel de seguridad: BAJO")

if __name__ == "__main__":
    print("=== GENERADOR DE CONTRASEÑAS ===")
    pwd = generar_contraseña()
    print(f"Contraseña generada: {pwd}\n")

    print("=== AUDITOR DE CONTRASEÑAS ===")
    auditar_contraseña(pwd)
