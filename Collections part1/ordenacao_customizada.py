from operator import attrgetter

nomes = ["guilherme", "Daniela", "Paulo", "Kaori"]

print(nomes)

print(sorted(nomes))


class ContaSalario:

    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False

        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        return self._saldo < outro._saldo

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)


conta_da_kaori = ContaSalario(9)
conta_da_kaori.deposita(1000)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(500)

conta_do_guilherme = ContaSalario(10)
conta_do_guilherme.deposita(510)

contas = [conta_da_kaori, conta_do_guilherme, conta_da_daniela]


def extrai_saldo(conta):
    return conta._saldo # < acessando direto o saldo, opcao muito ruim

# o problema nessa situação é que quebra a ideia do encapsulamento
print("Acessando os dados da classe com uma função")
for conta in sorted(contas, key=extrai_saldo):
    print(conta)


print("")
print("Acessando os dados com attrgetter")
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)


print("")
print("Utilizando magic method __lt__")
for conta in sorted(contas):
    print(conta)

print("")
print("Verificando se uma conta é maior > que a outra")
print(conta_do_guilherme > conta_da_kaori)

