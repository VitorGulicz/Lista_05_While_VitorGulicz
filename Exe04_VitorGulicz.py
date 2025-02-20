#EXE 004 - Faça um programa que peça o nome do convidado que o usuario deseja convidar para uma festa. Depois disso, exiba a mensagem "[nome] foi adicionado(a) com sucesso no 
# convite!" e adicione 1 à contagem.
#Em seguida, pergunte se ele quer convidar outra pessoa.
#Continue repetindo isso até que ele não queira mais convidar ninguém para a festa e, em seguida, mostre quantas pessoas foram convidas para a festa.
nomeConvidado=input("Digite o nome do convidado: ")
contagem=0
contagem=contagem+1
op=input("Deseja convidar mais alguem?(s ou n) ")
if "s" in op:
    while op =="s":
        nomeConvidado=input("Digite o nome do convidado: ")
        contagem=contagem+1
        op=input("Deseja convidar mais alguem?(s ou n) ")
print("Quantidades de convidados: ",contagem," -Vitor Gulicz")