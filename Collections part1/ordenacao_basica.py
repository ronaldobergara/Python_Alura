idades = [15, 87, 32, 65, 56, 32, 49, 37]

print(sorted(idades))

print(list(reversed(idades)))

print(sorted(idades, reverse=True))

print(list(reversed(sorted(idades))))


# altera a ordenacao direto na variavel
idades.sort()
print(idades)