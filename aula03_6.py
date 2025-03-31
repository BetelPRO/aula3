tim1 = input("Qual o time da casa?\n")
tim2 = input("Qual o adversário?\n")
gols1 = int(input(f"Quantos gols o {tim1} fez? "))
gols2 = int(input(f"Quantos gols o {tim2} fez? "))

if gols1 > gols2:
    print(f"O {tim1} venceu o jogo!!!")
else:
    if gols2 > gols1:
        print(f"O {tim2} ganhou o jogo!!!")
    else:
        print(f"O {tim1} empatou com o {tim2} dentro de casa")