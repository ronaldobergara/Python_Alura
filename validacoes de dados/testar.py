# from documento import Documento
#
# cpf = Documento.cria_documento("79679593029")
# print(cpf)
#
# cnpj = Documento.cria_documento("13191520000170")
# print(cnpj)

import re


padrao_molde = "(xx)aaaa-wwww"
padrao = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
texto = "iqghqiwgdqigdiqgd763trq8 11933345678 hh    qhwiu   bweoiheo 8871345678"

print("")
print("findall")
resposta = re.findall(padrao, texto)
print(resposta)

print("")
print("search")
resposta2 = re.search(padrao, texto)
print(resposta2.group())