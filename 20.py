def separar_pares_impares(numeros):
    pares = []
    impares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return pares, impares

def main():
    numeros = []
    
    print("Digite 20 números inteiros:")
    for i in range(20):
        numero = int(input(f"Digite o {i+1}º número: "))
        numeros.append(numero)
    
    pares, impares = separar_pares_impares(numeros)
    
    print("\nNúmeros digitados:")
    print(numeros)
    print("\nNúmeros pares:")
    print(pares)
    print("\nNúmeros ímpares:")
    print(impares)

if __name__ == "__main__":
    main()