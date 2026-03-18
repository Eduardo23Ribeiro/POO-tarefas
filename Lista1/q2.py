x = int(input('Digite um mês do ano entre 1 e 12: '))
match x:
    case 1:
        print('Janeiro, 1 Semestre')
    case 2:
        print('Fevereiro, 1 Semestre')
    case 3:
        print('Março, 1 Semestre')
    case 4:
        print('Abril, 2 Semestre')
    case 5:
        print('Maio, 2 Semestre')
    case 6:
        print('Junho, 2 Semestre')
    case 7:
        print('Julho, 3 Semestre')
    case 8:
        print('Agosto, 3 Semestre')
    case 9:
        print('Setembro, 3 Semestre')
    case 10:
        print('Outubro, 4 Semestre')
    case 11:
        print('Novembro, 4 Semestre')
    case 12:
        print('Dezembro, 4 Semestre')
    case _:
        print('Mês inválido')