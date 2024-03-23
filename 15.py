
populationA = float(input('Digite a quantidade de população da PRIMEIRA cidade: '))
growth_index_a = float(input('Digite o índice de crecimento da PRIMEIRA cidade: '))

populationB = float(input('Digite a quantidade de população da SEGUNDA cidade: '))
growth_index_b = float(input('Digite o índice de crecimento da SEGUNDA cidade: '))
qtd_years = 0

print(populationA < populationB)
print(growth_index_a > growth_index_b)

if populationA < populationB and growth_index_a > growth_index_b:
    while populationA < populationB:
        populationGrowthA = (populationA / 100) * growth_index_a
        populationA += populationGrowthA

        populationGrowthB = (populationB / 100) * growth_index_b
        populationB += populationGrowthB
        qtd_years += 1
elif populationB < populationA and growth_index_b > growth_index_a:
    while populationB < populationA:
        populationGrowthB = (populationB / 100) * growth_index_b
        populationB += populationGrowthB

        populationGrowthA = (populationA / 100) * growth_index_a
        populationA += populationGrowthA

        qtd_years += 1
else:
    print("não foi possivel calculcar")
    

print(qtd_years == 0 if 'acho que não é possivel calcular o crecimento.' else qtd_years)

