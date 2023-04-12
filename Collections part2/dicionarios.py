aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

print("Conteudo do dicionario")
print(aparicoes)

print("")
print("Tipo")
print(type(aparicoes))

print("")
print("Valor da chave Guilherme")
print(aparicoes["Guilherme"])

print("")
print("Valor da chave cachorro")
print(aparicoes["cachorro"])

# Quando a chave não existe no dicionario retorna uma exception, para essas situações se utiliza o get
#print(aparicoes["xpto"])

print("")
print("Buscando um valor utilizando uma chave que não existe com get e definido um valor padrão 0 caso nao exista")
print(aparicoes.get("xpto", 0))

print("")
print("buscando valor com a chave cachorro com o get")
print(aparicoes.get("cachorro", 0))

# uma segunda forma de criar variaveis dict
aparicoes = dict(Guilherme = 2, cachorro = 1)
print(aparicoes)

aparicoes = {
  "Guilherme" : 1,
  "cachorro" : 2,
  "nome" : 2,
  "vindo" : 1
}

print("")
print("Alterando valor da chave Carlos para 1")
aparicoes["Carlos"] = 1
print(aparicoes)

print("")
print("Alterando valor da chave Carlos para 2")
aparicoes["Carlos"] = 2
print(aparicoes)

print("")
print("Deletando a chave Carlos do nosso dicionario utilizando del")
del aparicoes["Carlos"]
print(aparicoes)

print("")
print("Verificando com in se existe a chave cachorro")
print("cachorro" in aparicoes)

print("")
print("Verificando com in se existe a chave Carlos")
print("Carlos" in aparicoes)


print("")
print("For no nosso dicionario")
for elemento in aparicoes:
  print(elemento)

print("")
print("For no nosso dicionario puxando somente as chaves")
for elemento in aparicoes.keys():
  print(elemento)

print("")
print("For no nosso dicionario puxando somente os valores")
for elemento in aparicoes.values():
  print(elemento)

print("")
print("Verificando com in se existe o valor 1 ")
print(1 in aparicoes.values())


print("")
print("For no nosso dicionario puxando somente a chaves e passando a chave para pegar o valor")
for elemento in aparicoes.keys():
  valor = aparicoes[elemento]
  print(elemento, valor)

print("")
print("For no nosso dicionario nos itens para pegar chave e valor")
for elemento in aparicoes.items():
  print(elemento)

print("")
print("For no nosso dicionario, despacotando chave e valor")
for chave, valor in aparicoes.items():
  print(chave, "=", valor)

print("")
print("For com list comprehension")
print(["palavra {}".format(chave) for chave in aparicoes.keys()])