#Crie uma variável chamada “adivinha” e defina o valor como 50. 
#Peça ao usuário para inserir um número. Embora o palpite não seja o mesmo que o valor do “adivinha”, diga a ele se o palpite é muito baixo ou muito alto e peça que 
# ele dê outro palpite. 
#Se ele inserir o mesmo valor que “adivinha”, exiba a mensagem "Parabéns! Você acertou o número em {} tentativas!".
advinha=50
chute=int(input("Digite um numero: "))
if chute<=20:
    print("Palpite muito baixo!")
elif chute>=80:
    print("Palpite muito alto!")
contagem=0
contagem=contagem+1
while chute!=advinha:
        chute=int(input("Digite um numero: "))
        if chute<=20:
            print("Palpite muito baixo!")
            contagem=contagem+1
        elif chute>=80:
            print("Palpite muito alto!")
            contagem=contagem+1
        else:
             contagem=contagem+1   
print("Parabéns! Você acertou o número em {} tentativas! -Vitor Gulicz".format(contagem))