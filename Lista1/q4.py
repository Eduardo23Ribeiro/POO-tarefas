dia = int(input('escreva o dia: '))
mes = int(input('escreva o mês: '))
ano = int(input('escreva o ano: '))

data_valida = True

 
if not (mes >= 1 and mes <= 12):
    data_valida = False

if data_valida:
    if mes == 1:
        if not (1 <= dia <= 31):
            data_valida = False
    if mes == 2:
        if not (1 <= dia <= 28):
            data_valida = False
    if mes == 3:
        if not (1 <= dia <= 31):
            data_valida = False
    if mes == 4:
        if not (1 <= dia <= 30):
            data_valida = False
    if mes == 5:
        if not (1 <= dia <= 31):
            data_valida = False
    if mes == 6:
        if not (1 <= dia <= 30):
            data_valida = False
    if mes == 7:
        if not (1 <= dia <= 31):
            data_valida = False
    if mes == 8:
        if not (1 <= dia <= 31):
            data_valida = False
    if mes == 9:
        if not (1 <= dia <= 30):
            data_valida = False
    if mes == 10:
        if not (1 <= dia <= 31):
            data_valida = False
    if mes == 11:
        if not (1 <= dia <= 30):
            data_valida = False
    if mes == 12:
        if not (1 <= dia <= 31):
            data_valida = False

if not (1900 <= ano <= 2100):
    data_valida = False

if data_valida:
    print(f'{dia:02d}/{mes:02d}/{ano:02d}')

else:
    print('A data informada não é válida')