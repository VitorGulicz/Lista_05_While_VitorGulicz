#Faça um programa que leia os numeros digitados pelo usuario, a cada numero digitado ele deve ser somado ao anterior e a cada soma deve ser exibida na tela. Quando a soma for 
# superior a 50 ele deve exibir a mensagem "o total é :" e parar o programa 
soma=0
while soma<=50:
    numero=int(input("Digite um numero: "))
    soma+=numero
print("O total é: ",soma, " -Vitor Gulicz")