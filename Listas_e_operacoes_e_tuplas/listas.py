idades = [3, 28, 38]

print("")
print('Imprimindo valores de uma lista')
print(idades)

print("")
print('Imprimindo valor em uma posição')
print(idades[0])

print("")
print('Imprimindo lista de idades')
for idade in idades:
    print(idade)

# Doc referente a Listas e seus metodos
# https://docs.python.org/3/tutorial/datastructures.html

print("")
print('Usando metodo append para adicionar um novo valor no final da lista')
idades.append(10)
print(idades)


print("")
print('Usando metodo remove para remover um valor da lista')
idades.remove(3)
print(idades)

print("")
print('Utiliza "in" para verificar se um valor existe na lista antes de remover')
if 3 in idades:
    idades.remove(3)
print(idades)

print("")
print('Utiliza metodo insert para adicionar um elemento na posição desejada, vamos adicionar 42 na primeira posição')
idades.insert(0, 42)
print(idades)

print("")
print('Utiliza metodo extend para adicionar os valores de uma nova lista dentro da nossa lista')
nova_lista = [60, 61, 62]
print('Nossa lista com valores atual')
print(idades)
print('Nova lista com novos valores')
print(nova_lista)
idades.extend(nova_lista)
print('Agora nossa lista com os novos valores, utilizando o extend para unir com os novos valores')
print(idades)

print("")
print("list comprehension")
print("Criando uma nova lista adicionando + 1 nos valores com for em uma linha")
nova_lista = [idade+1 for idade in idades]
print("Nova lista com +1")
print(nova_lista)


print("")
print("Criando uma nova lista com valores igual ou maior que 60")
print(idades)
nova_lista.clear()
nova_lista = [idade for idade in idades if idade >= 60]
print("Nova lista com valores maior ou igual a 60")
print(nova_lista)

print("")
print("Utilizando função junto com list comprehension para aumentar + 1 na idade e retornar a idade meno que 60")
def proximo_ano(idade):
    return idade+1
print("Nossa lista sem aumentar + 1 na idade")
print(idades)
nova_lista.clear()
nova_lista = [proximo_ano(idade) for idade in idades if idade < 60]
print("Nossa lista com + 1 na idade com valores menor que 60")
print(nova_lista)
