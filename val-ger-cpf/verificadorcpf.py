"""
CPF = 168.995.350-09
-------------------------------------------------------------------------
1 * 10 = 10                 #       1 * 11 = 11
6 * 9 = 54                  #       6 * 10 = 60
8 * 8 = 64                  #       8 * 9 = 72
9 * 7 = 63                  #       9 * 8 = 72
9 * 6 = 54                  #       9 * 7 = 63
5 * 5 = 25                  #       5 * 6 = 30
3 * 4 = 12                  #       3 * 5 = 15
5 * 3 = 15                  #       5 * 4 = 20
0 * 2 = 0                   #       0 * 3 = 0
                            #->     0 * 2 = 0
       297                  #             343
11 - (297 % 11) = 11        #       11 - (343 % 11) = 9
11 > 9 = 0                  #
Digito 1 = 0                #  Digito 2 = 9
"""
while True:
    cpf_digitado = input("Digite seu cpf: ")
    multiplicacao_1 = 10
    multiplicacao_2 = 11
    soma1 = 0
    soma2 = 0
    listacpf = []
    r_1 = []
    r_2 = []

    # Retirar os '.' e o '-' do cpf e armazenar numa lista vazia (listacpf)
    for x in cpf_digitado:
        if x == '.' or x == '-':
            pass
        else:
            listacpf.append(x)

    # Iterar a listacpf para fazer a multiplicacão decrescente a partir de 10 e armazenar os dados na lista vazia r_1
    for y in listacpf:
        if multiplicacao_1 > 1:
            m = int(y) * multiplicacao_1
            multiplicacao_1 -= 1
            r_1.append(m)
        else:
            pass

    # Soma dos valores da lista r_1
    for z in r_1:
        soma1 = z + soma1

    # Formula para verificação do penúltimo dígito e utilização do if para essa verificação.
    formula1 = 11-(soma1 % 11)
    if formula1 > 9:
        if listacpf[-2] == '0':
            pass
        else:
            print(f"O penúltimo dígito {listacpf[-2]} está errado")
            continue
    elif formula1 <= 9:
        formula1 = str(formula1)
        if listacpf[-2] == formula1:
            pass
        else:
            print(f"O penúltimo dígito {listacpf[-2]} está errado.")
            continue

    # Iterar a lista cpf para segunda validação com a multiplicação decrescente a partir de 11 e armazenar os dados na
    # lista vazia r_2
    for n in listacpf:
        if multiplicacao_2 > 1:
            i = int(n) * multiplicacao_2
            multiplicacao_2 -= 1
            r_2.append(i)
        else:
            pass

    # Soma dos valores da lista r_2
    for t in r_2:
        soma2 = t + soma2

    # Fórmula para verificação do último dígito e validação de CPF
    formula2 = 11-(soma2 % 11)
    if listacpf[-1] != str(formula2):
        if formula2 > 9 and listacpf[-1] == '0':
            print(f'CPF {cpf_digitado} validado!')
        else:
            print(f"O último dígito {listacpf[-1]} está errado!")
            continue
    else:
        print(f'CPF {cpf_digitado} validado!')












