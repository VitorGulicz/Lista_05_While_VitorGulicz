#Escreva um programa que permaneça em laço lendo números inteiros. 
#O laço termina quando for digitado 0 (zero).
#Cada valor diferente de zero digitado deve ser colocado em uma lista, desde que ele ainda não esteja lá, ou seja, valores repetidos não são aceitos. 
#Se um valor repetido for digitado, o programa deve exibir uma mensagem na tela. 
#Ao final exiba a lista e a quantidade de elementos que ela contém.
numero=input("Digite um numero: ")
numeros=[]
numeros.append(numero)
while numero !="0":
    numero=input("Digite um numero: ")
    if numero in numeros:
        print("Numero repitido")
    else:
        numeros.append(numero)
lista=len(numeros)
print("Os numeros cadastrados foram {} e possui {} numeros -Vitor Gulicz".format(numeros,lista))