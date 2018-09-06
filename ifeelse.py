
#!/usr/bin/python3

# nota1 = input('Digite a nota 01: ')
# nota2 = input('Digite a nota 02: ')

# #nota1 = int(input('Digite a nota 01: '))
# #nota2 = int(input('Digite a nota 02: '))

# nota1 = int(nota1)
# nota2 = int(nota2)

# media = (nota1 + nota2) / 2

notas = int(input('Digite o numero de Notas: '))

soma = 0
for x in range (notas):
    nota = int(input('digite n{} '.format(x+1)))
    soma += nota
media = soma / notas

if media >= 7:
    print('Media {}, aprovado'.format(media))
elif media >3:
    print('Media {}, recuperacao'.format(media))
else:
    print('Media {}, reprovado'.format(media))


