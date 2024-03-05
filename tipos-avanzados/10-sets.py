# un set es un grupo o un conjunto
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]

# lista a set
segundo = set(segundo)

# Union de sets
print(primer | segundo)

# Interseccion de set
print(primer & segundo)

# Diferencia de set
print(primer - segundo)

# Diferencia simetrica de set
print(primer ^ segundo)

# metodos basicos le los sets
# primer.add(5)
# primer.remove(1)
# print(primer)
