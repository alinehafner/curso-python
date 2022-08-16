import random


lista = []
with open('palavras.txt', 'r') as arquivo:
    for z in arquivo:
        lista += z.split()
palavra_r = random.choice(lista)
i = len(palavra_r) + 1
print(f'A palavra tem {len(palavra_r)} letras. Você tem {i} chances para acertar! ')

final = [x for x in '*' * len(palavra_r)]


def jogo(n: int, arg):
    while n > 0:
        tentativa = input('Digite sua primeira tentativa:')
        if len(tentativa) == len(arg):
            if tentativa == arg:
                print(f'Parabéns você acertou! A palavra de hoje era {arg}!')
                break
            else:
                p = 0
                p_l = []
                i = 0
                i_l = []
                for z in range(len(arg)):
                    if tentativa[z] in arg:
                        if tentativa[z] == arg[z]:
                            p += 1
                            final[z] = arg[z]
                            p_l.append(tentativa[z])
                        else:
                            if tentativa.count(tentativa[z]) != arg.count(arg[z]) and tentativa.index(tentativa[z]) == arg.index(tentativa[z]):
                                pass
                            else:
                                i += 1
                                i_l.append(tentativa[z])
                n -= 1
                print(f'{p} letra(s) certas --{p_l}--, e {i} em lugares diferentes --{i_l}--!')
                print(f'Você ainda tem {n} tentativas')
                print("".join(final))
        else:
            print(f'Digite uma palavra com {len(arg)} letras.')

    if (n == 0) and (final != arg):
        print(f'Você perdeu! A palavra era {arg}')


jogo(i, palavra_r)
