contador=1
impar=0
par=0
while contador<=10:
    numero=int(input("Digite um numero inteiro: "))
    contador=contador+1
    if numero%2==0:
        par=par+1
    else:
        impar=impar+1
print(f"Há {par} números pares e {impar} números ímpares")
