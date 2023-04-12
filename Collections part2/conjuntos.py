usuarios_data_science = [15, 23, 43, 56]
usuarios_machine_learning = [13, 23, 56, 42]

assistiram = usuarios_data_science.copy()
assistiram.extend(usuarios_machine_learning)
assistiram

print(len(assistiram))

print(set(assistiram))

print(set([1,2,3,1]))

print({4, 1,2,3,1})

print(type({1,2}))

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_machine_learning)


for usuario in set(assistiram):
  print(usuario)

usuarios_data_science = {15, 23, 43, 56}
usuarios_machine_learning = {13, 23, 56, 42}

print(usuarios_data_science)
print(usuarios_machine_learning)
print("")
print("Operação de ou em conjuntos, pega todos elementos de ambos")
print(usuarios_data_science | usuarios_machine_learning)

print("")
print("Operação de & em conjuntos, elementos que tem em 1 e no outro")
print(usuarios_data_science & usuarios_machine_learning)

print("")
print("Operação de - em conjuntos, elementos que tem em um e não tem no outro")
print(usuarios_data_science - usuarios_machine_learning)

fez_ds_mas_nao_fez_ml = usuarios_data_science - usuarios_machine_learning
15 in fez_ds_mas_nao_fez_ml

23 in fez_ds_mas_nao_fez_ml

usuarios_data_science ^ usuarios_machine_learning