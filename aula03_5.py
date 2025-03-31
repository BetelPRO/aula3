n1 = float(input("Primeira nota: "))
n2 = float(input("Segunda nota: "))
n3 = float(input("Terceira nota: "))
media = (n1+n2+n3)/3
"""
if n1 < 0  or n2 < 0 or n3 < 0:
    print("números inválidos")
elif n1 > 10  or n2 > 10 or n3 > 10:
    print("números inválidos")
elif media >= 7:
    print("Aprovado")
elif 4 <= media < 7:
    print("recuperação")
else:
    print("Reprovado")
"""
if media >= 7:
    print(f"Aprovado, {media:.2f}")
else:
    if media < 4:
        print(f"Reprovado, {media:.2f}")
    else:
        print(f"Recuperação, {media:.2f}")