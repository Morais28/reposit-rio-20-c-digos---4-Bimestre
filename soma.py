soma = 0 #variável que guarda a soma acumulada
cont = 0 #contador de quantos números já pedimos

while cont < 5:               #repetir5 vezes
    numero = float(input("Digite um número:  ")) #alê o número
    soma += numero #soma= soma + numero
    cont += 1             #aumenta o contador

print("soma final:", soma)