print("Qual o limite inferior?\n")
LInf=int(input())

print("Qual o valor superior?\n")
LSup=int(input())

while LInf > LSup:
    print("Limites escolhidos estão errados, por favor tente de novo\n")
    print("Qual o limite inferior?\n")
    LInf=int(input())

    print("Qual o valor superior?\n")
    LSup=int(input())
    
while LSup >= LInf:
    print("Números no intervalo: ", LInf)
    LInf = LInf + 1