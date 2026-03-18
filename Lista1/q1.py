a = int(input())
b = int(input())
c = int(input())
d = int(input())
sp = 0
si = 0

if a % 2 == 0: 
    sp += a 
else: 
    si += a
if b % 2 == 0:
     sp += b
else: 
    si += b
if c % 2 == 0:
     sp += c
else: 
    si += c
if d % 2 == 0:
     sp += d 
else:
    si += d
print("soma dos pares ", sp)
print("soma dos impares ", si)