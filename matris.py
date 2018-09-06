#!/usr/bin/python3

matris = [
    [1, 3, 6],
    [3, 5, 7],
    [6, 9, 11]
]

cont = 0
a = 0
b = 0
for cont, x in enumerate(matris):
    a += x[cont]
    b += x[-(cont+1)]
    cont += 1

print(a + b)

