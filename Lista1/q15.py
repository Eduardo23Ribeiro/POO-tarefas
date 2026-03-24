def Primo(n):
    if n <= 1:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

num = int(input("Valor: "))

if Primo(num):
    print("É primo")
else:
    
    print("Não é primo")