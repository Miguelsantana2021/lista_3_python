def multiplos_no_intervalo(multiplo, limite):
    numero = multiplo 
    print(numero, end=", ")
    numero += multiplo   
multiplo = int(input("Digite o número múltiplo: "))
limite = int(input("Digite o limite: "))
print("Números múltiplos de", multiplo, "no intervalo de 0 a", limite, ":")
multiplos_no_intervalo(multiplo, limite)