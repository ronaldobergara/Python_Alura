import re

endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120"

padrao = re.compile("[0-9]{5}[-]{0,1}[0-9]{3}")

busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)
else:
    raise ValueError("Não foi encontrado o padrão")


''''
Exemplos de URLs válidas:
    bytebank.com/cambio
    bytebank.com.br/cambio
    www.bytebank.com/cambio
    www.bytebank.com.br/cambio
    http://www.bytebank.com/cambio
    http://www.bytebank.com.br/cambio
    https://www.bytebank.com/cambio
    https://www.bytebank.com.br/cambio

Exemplos de URL inválidas:
    https://bytebank/cambio
    http://bytebank.naoexiste/cambio
    ht:bytebank.naoexiste/cambio

'''

url = "https://www.bytebank.com.br/cambio"

url_padrao = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
match = url_padrao.match(url)

if not match:
    raise ValueError("A URL não é válida.")