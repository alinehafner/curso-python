from random import randint

gerador = randint(100000000, 999999999)
lista1 = []
m1 = []
m2 = []
total1 = 0
total2 = 0
var1 = 10
var2 = 11
cpf = ''

for x in str(gerador):
    lista1.append(x)
for y in lista1:
    z = int(y) * var1
    var1 -= 1
    m1.append(z)
for t1 in m1:
    total1 = t1 + total1
formula1 = 11-(total1 % 11)
if formula1 > 9:
    lista1.append('0')
elif formula1 <= 9:
    lista1.append(str(formula1))
for k in lista1:
    o = int(k) * var2
    var2 -= 1
    m2.append(o)

for t2 in m2:
    total2 = t2 + total2
formula2 = 11-(total2 % 11)
if formula2 > 9:
    lista1.append('0')
elif formula2 <= 9:
    lista1.append(str(formula2))
for i in lista1:
    cpf = cpf + i

print("CPF gerado: ", end = '')
print(cpf[0:3], cpf[3:6], cpf[6:9], sep = '.', end = '-')
print(cpf[9:12])

