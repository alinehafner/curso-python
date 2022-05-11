import random

def inicial():
    cnpj_1 = ''
    for i in range(8):
        aleatorio = random.randint(0, 9)
        cnpj_1 += str(aleatorio)
    cnpj_1 += '0001'
    return cnpj_1


def primeiro_digito():
    cnpj_1 = inicial()
    validador_1 = '543298765432'
    soma = 0
    for i in range(len(cnpj_1)):
        soma += int(cnpj_1[i]) * int(validador_1[i])
    formula = 11 - (soma % 11)
    if formula > 9:
        cnpj_1 += '0'
    else:
        cnpj_1 += str(formula)
    return cnpj_1


def segundo_digito():
    cnpj_2 = primeiro_digito()
    validador_2 = '6543298765432'
    soma = 0
    for i in range(len(cnpj_2)):
        soma += int(cnpj_2[i]) * int(validador_2[i])
    formula = 11 - (soma % 11)
    if formula > 9:
        cnpj_2 += '0'
    else:
        cnpj_2 += str(formula)
    return cnpj_2


def formata(string):
    string = f'{string[:2]}.{string[2:5]}.{string[5:8]}/{string[8:12]}-{string[12:]}'
    return string


def gerador():
    cnpj_gerado = segundo_digito()

    return formata(cnpj_gerado)

