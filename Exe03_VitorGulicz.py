#Peça ao usuário para inserir um número e, em seguida, insira outro número. Some esses dois números e pergunte se ele quer adicionar outro número.
#Se ele digitar “ s ", diga para inserir outro número e continuar adicionando números e somando até que ele não respondam “ s ".
#Depois que o loop for interrompido, exiba o total.

numero=int(input("Digite um numero: "))
soma=0
soma=soma+numero
numero=int(input("Digite outro numero: "))
soma=soma+numero
op=input("Deseja adicionar um numero?(s ou n)")
while op =="s":
    numero=int(input("Digite um numero: "))
    soma=soma+numero
    op=input("Deseja adicionar um numero?(s ou n)")
print("A soma dos numeros é",soma," -Vitor Gulicz")