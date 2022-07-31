from random import choice
entrada = sorted(list(map(int, input().split())))
totais = [int(str(i)+str(entrada[z])) for i in entrada for z in range(len(entrada)) if not int(str(i)+str(entrada[z])) == 0 if not int(str(i)+str(entrada[z])) > 60]

for y in range(7):
    copia = totais.copy()
    jogos = []
    for z in range(6):
        ran = choice(copia)
        copia.remove(ran)
        jogos += [ran]
    print(sorted(jogos))

