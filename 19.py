def eh_consoante(caractere):
    consoantes = "AEIOUaeiou"
    return caractere in consoantes

def main():
    caracteres = []

    print("Digite 10 caracteres:")
    for i in range(10):
        caractere = input(f"Digite o {i+1}º caractere: ")
        caracteres.append(caractere)

    consoantes = [caractere for caractere in caracteres if eh_consoante(caractere)]
    print(f"\nForam lidas {len(consoantes)} consoantes.")
    print("Consoantes lidas:")
    print(consoantes)

if __name__ == "__main__":
    main()