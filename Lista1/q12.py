import math


def MenorInteiro(x):
    inteiro_x = int(x)
    if x <= inteiro_x:
        return inteiro_x
        
    else:
        return inteiro_x + 1
print(MenorInteiro(6.77777777777777))


# ####
# def MenorInteiro2(x):
#     return math.ceil(x)
# print(MenorInteiro2())
