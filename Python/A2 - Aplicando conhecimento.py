import math
custo_espetaculo = float(input("Digite o custo do espetáculo: "))
preco_convite = float(input("Digite o preço do convite: "))
convites_custo = math.ceil(custo_espetaculo / preco_convite)
lucro_desejado = custo_espetaculo * 0.23
convites_lucro = math.ceil((custo_espetaculo + lucro_desejado) / preco_convite)
print(convites_custo)
print(convites_lucro)