nombre_curso = 'ultimate course'
descripcion = """
este nos permite escribir textos muy largos
y tener saltos de linea y   tabs sin agregar su caracter especia
"""

# dos formas de usar el print
print(nombre_curso, descripcion)
print(f'{nombre_curso} {descripcion}')

len(nombre_curso)   # Nos da la longitud del argumento que le demos
print(len(nombre_curso))

# Accedemos al caracter que le indicamos como indice
print(nombre_curso[4])

# Cortamos una cadena, le indicamos donde queremos iniciar a cortar y hasta donde queremos cortar
print(nombre_curso[0:8])

# Cortamos una cadena, desde el indice indicado hasta el final de la cadena
print(nombre_curso[9:])

# Cortamos una cadena, desde el inicio de la cadena hasta el indice indicado
print(nombre_curso[:9])

# Imprime la cadena sin cortar
print(nombre_curso[:])
