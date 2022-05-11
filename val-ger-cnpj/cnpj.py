def formatar(string):
    string = string.replace('.', '')
    string = string.replace('-', '')
    string = string.replace('/', '')
    return string


def digitos(string):
    return string[0:12]


def valida1(string):
    string = digitos(string)
    validador1 = '543298765432'
    soma = 0
    for i in range(len(string)):
        soma += int(string[i]) * int(validador1[i])
    formula = 11 - (soma % 11)
    if formula > 9:
        string += '0'
    else:
        string += str(formula)
    return string


def valida2(string):
    string = valida1(string)
    validador1 = '6543298765432'
    soma = 0
    for i in range(len(string)):
        soma += int(string[i]) * int(validador1[i])
    formula = 11 - (soma % 11)
    if formula > 9:
        string += '0'
    else:
        string += str(formula)
    return string


def validador(string):
    string_inicial = formatar(string)
    repeticao = string[0] * len(string)
    if repeticao == string:
        return False
    else:
        try:
            string_verificar = valida2(string_inicial)
        except:
            return False

    if string_inicial == string_verificar:
        return True
    else:
        return False



