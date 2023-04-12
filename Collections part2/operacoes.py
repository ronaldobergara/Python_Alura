usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))

usuarios.add(13)
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))

usuarios

usuarios = frozenset(usuarios)
print(usuarios)

print(type(usuarios))

# quando utiliza frozenset não permite alterar o conjunto.
# usuarios.add(134)

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
print(meu_texto.split())

print(set(meu_texto.split()))