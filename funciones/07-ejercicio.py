# Corregir codigo
def es_palindromo(frase):
    reverse = ''
    sin_espacios = frase.lower()
    for letra in range(len(sin_espacios)):
        # print(sin_espacios[-1-letra])
        reverse += sin_espacios[-1-letra]
    print(frase, reverse)
    return reverse.lower() == frase


print(es_palindromo('Reconocer'))
