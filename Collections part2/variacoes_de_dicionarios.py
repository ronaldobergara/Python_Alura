meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto = meu_texto.lower()

print("")
print("texto")
print(meu_texto)

aparicoes = {}

for palavra in meu_texto.split():
  ate_agora = aparicoes.get(palavra, 0)
  aparicoes[palavra] = ate_agora + 1

print("")
print("Contagem de palavras utilizando get")
print(aparicoes)

from collections import defaultdict

aparicoes = defaultdict(int)

for palavra in meu_texto.split():
  ate_agora = aparicoes[palavra]
  aparicoes[palavra] = ate_agora + 1

print("")
print("Contagem de palavras utilizando defaultdict")
print(aparicoes)

int()

dicionario = defaultdict(int)
dicionario['guilherme']

dicionario['guilherme'] = 15
dicionario['guilherme']

aparicoes = defaultdict(int)

print("")
print("Simplificando a contagem de palavras no for utilizando defaultdict")
for palavra in meu_texto.split():
  aparicoes[palavra] += 1

print(aparicoes)

class Conta:
  def __init__(self):
    print("Criando uma conta")

contas = defaultdict(Conta)

print("")
print("Criando a classe conta com defaultdict")
print(contas[15])

print(contas[17])

print(contas[15])

from collections import Counter

print("")
print("Utilizando counter para contar as palavras e simplificando ainda a mais o for")
aparicoes = Counter()
for palavra in meu_texto.split():
  aparicoes[palavra] += 1

print(aparicoes)

print("")
print("Utilizando counter para contar as palavras em uma linha sem o for")
aparicoes = Counter(meu_texto.split())
print(aparicoes)

