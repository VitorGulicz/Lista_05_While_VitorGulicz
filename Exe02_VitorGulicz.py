#Peça ao usuario para inserir um numero. Continue perguntando até que ele insira 5 numeros e em seguida exiba a mensagem "o ultimo numero que voce digitou foi: " e pare o programa
i=0
while i<=4:
    numero=int(input("Digite um numero: "))
    i+=1
print("O ultimo numero digitado foi: ",numero," -Vitor Gulicz")