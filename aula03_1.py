nome = input("Digite o seu nome: ")
idade = int(input(f"Olá {nome}, qual a sua idade?\n"))
salario = float(input("Quanto você recebe?\n"))
aumento = float(input("Qual o percentual de aumento desejado?\n"))
calculo = salario/100*aumento
print(f"Dados do usuário:\n{nome} - {idade} anos\nSalário R$ = {salario:.2f}\nAumento desejado {aumento}\n---Novo salário---\n{calculo+salario:.2f}")