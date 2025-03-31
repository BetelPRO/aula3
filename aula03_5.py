n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
media = (n1+n2+n3)/3

if media >= 7:
    print("Aprovado")
elif n1 < 0  or n2 < 0 or n3 < 0:
    print("numeros invalidos")
else:
    print("Reprovado")