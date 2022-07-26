"""
https://www.todoespacoonline.com/w/2015/calculo-de-sub-redes-ipv4/
"""


class Ipv4:
    def __init__(self, ip, bits=26):
        self.ip = ip
        self.bits = bits
        self.lista = [128, 64, 32, 16, 8, 4, 2, 1]

    # Getter
    @property
    def ip(self):
        return self._ip

    # Setter
    @ip.setter
    def ip(self, valor):
        self._ip = valor.split(".")

    def converter_bin(self):
        num = []
        for i in range(len(self.ip)):
            seq = ''
            sub = int(self.ip[i])
            for z in self.lista:
                if z > sub:
                    seq += '0'
                else:
                    if sub - z == 0:
                        seq += '1' + '0'*(abs(self.lista.index(z)-len(self.lista))-1)
                        break
                    else:
                        sub = sub - z
                        seq += '1'
            num += [seq]
        return num

    def transformada(self):
        lis_bin = "".join(self.converter_bin())
        transformada = lis_bin[:self.bits].replace("0", "1") + lis_bin[self.bits:].replace('1', '0')
        sep_trans = [transformada[i:i + 8] for i in range(0, len(transformada), 8)]
        return sep_trans

    def mascara(self):
        sep_trans = self.transformada()
        mascara = ''
        for i in sep_trans:
            if i.count('1') == 8:
                mascara += str(sum(self.lista)) + "."
            else:
                mascara += str(sum(self.lista[:i.count('1')]))
        return mascara

    def rede(self):
        ip_copia = self.ip.copy()
        zeros = "".join(self.transformada()).count('0')
        lis_bin = self.converter_bin()
        lis_bin[-1] = str(lis_bin[-1][:len(lis_bin[-1])-zeros]) + '0'*zeros
        num = 0
        for z in range(len(lis_bin[-1])):
            num += self.lista[z] * int(lis_bin[-1][z])
        ip_copia.pop()
        ip_copia.append(str(num))
        return ip_copia

    def broadcast(self):
        ip_copia = self.ip.copy()
        zeros = "".join(self.transformada()).count('0')
        lis_bin = self.converter_bin()
        lis_bin[-1] = str(lis_bin[-1][:len(lis_bin[-1]) - zeros]) + '1' * zeros
        num = 0
        for z in range(len(lis_bin[-1])):
            num += self.lista[z] * int(lis_bin[-1][z])
        ip_copia.pop()
        ip_copia.append(str(num))
        return ip_copia

    def host(self):
        conv_bin = "".join(self.converter_bin())
        numeros = 2 ** (len(conv_bin) - self.bits) - 2
        return numeros


ip1 = Ipv4('192.168.0.1', 26)
print(f'Ip: {".".join(ip1.ip)}')
print(f'Máscara: {ip1.mascara()}')
print(f'Rede: {".".join(ip1.rede())}')
print(f'Broadcast: {".".join(ip1.broadcast())}')
print(f'Prefixo: {ip1.bits}')
print(f"Número de Ip's de rede: {ip1.host()} ")




