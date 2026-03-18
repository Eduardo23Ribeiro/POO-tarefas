v1 = int(input('escreva um valor: '))
v2 = int(input('escreva um valor: '))
v3 = int(input('escreva um valor: '))

if v1 > v2:
    v1, v2 = v2, v1

if v1 > v3:
    v1, v3 = v3, v1

if v2 > v3:
    v2, v3 = v3, v2

print(f'{v1}, {v2}, {v3}')