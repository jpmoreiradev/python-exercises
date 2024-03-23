
populationA = 80000
populationB = 200000
qtd_years = 0

while populationA < populationB:
    populationGrowthA = (populationA / 100) * 3
    populationA += populationGrowthA

    populationGrowthB = (populationB / 100) * 1.5
    populationB += populationGrowthB
    qtd_years += 1

print(qtd_years)

