animal = 'copiTo michi'
animal2 = '   copiTo michi  '


# Metodos de strings
# Todo a mayusculas
print(animal.upper())

# Todo a minusculas
print(animal.lower())

# Primera letra mayuscula
print(animal.capitalize())

# Primera letra mayuscula de cada palabra del string
print(animal.title())

# Quita los espacios en blanco al principio y al final de la cadena
print(animal2.strip())

# Encadenando metodos
print(animal2.strip().capitalize())

# Quita los espacios en blanco al final de la cadena
print(animal2.rstrip())

# Quita los espacios en blanco al principio de la cadena
print(animal2.lstrip())

# Devuelve el indice de donde se encuentre lo que buscamos en la cadena
print(animal.find('To'))

# Si no lo encuentra me devuelve un -1
print(animal.find('ap'))

# Reemplaza el primer argumento que le pasamos (si es que la cadena lo tiene) por el segundo argumento
print(animal.replace('pi', 'fi'))

# Valida si la cadena dada se encuentra en nuestra variable animal
print('pi' in animal)

# Valida si la cadena dada no se encuentra en la variable animal
print('fi' not in animal)
