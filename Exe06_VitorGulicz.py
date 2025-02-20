#Peça ao usuário para inserir um número entre 15 e 20.
#Se ele inserir um valor abaixo de 15, exiba a mensagem "Muito baixo" e peça que tentem novamente.
#Se ele inserir um valor acima de 20, exiba a mensagem "Muito alto" e peça que tentem novamente.
#Continue repetindo isso até que ele insira um valor entre 15 e 20 e, em seguida, exibam a mensagem "Obrigado".
chute=int(input("Digite um numero: "))
if chute<=15:
    print("Muito baixo!")
elif chute>=20:
    print("Muito alto!")
while 15<chute<20:
        chute=int(input("Digite um numero: "))
        if chute<=20:
            print("Palpite muito baixo!")
        elif chute>=15:
            print("Numero muito alto!")   
print("Obrigado!")