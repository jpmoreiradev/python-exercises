def somaImposto(taxaImposto, custo):
    resultado_imposto = custo + (custo * taxaImposto / 100)
    return resultado_imposto

taxaImposto = float(input("Digite a taxa de imposto sobre vendas (em porcentagem): "))
custo = float(input("Digite o custo do item antes do imposto: "))

resultado = somaImposto(taxaImposto, custo)
print("O custo com imposto é:", resultado)
