v1 = int(input("Digite o primeiro valor: "))
v2 = int(input("Digite o segundo valor: "))
v3 = int(input("Digite o terceiro valor: "))
v4 = int(input("Digite o quarto valor: "))

valor = [v1, v2, v3, v4]

if len(set(valor)) != 4:
    print("Erro: Os valores não são todos diferentes!")

else:
    valor.sort()

    menor = valor[0]          
    seg_menor = valor[1]  
    seg_maior = valor[2]   
    maior = valor[3]          

    soma_dos_segs = seg_maior + seg_menor

    print(f"Maior valor = {maior}")
    print(f"Menor valor = {menor}")
    print(f"A soma do segundo maior valor com o segundo menor = {soma_dos_segs}")