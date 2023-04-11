from operator import attrgetter
from functools import total_ordering

@total_ordering
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
conta_do_guilherme.deposita(500)

contas = [conta_da_kaori, conta_do_guilherme, conta_da_daniela]


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

print("")
print("Aplicando na ordenacao + de um campo com attrgetter, caso a conta tenha o mesmo saldo, ordena pelo código")
for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
    print(conta)

print("Adicionado o decorator @total_order para ser possivel fazer qualquer tipo de comparação <, > ou ==")
print(conta_do_guilherme < conta_da_kaori)
print(conta_do_guilherme == conta_da_daniela)