print("Qual o limite inferior?\n")
LInf=int(input())

print("Qual o valor superior?\n")
LSup=int(input())

if LInf > LSup:
    print("Limites escolhidos estão errados, por favor tente de novo\n")
    print("Qual o limite inferior?\n")
    LInf=int(input())

    print("Qual o valor superior?\n")
    LSup=int(input())
    
elif LSup > LInf:
    for i in range(LInf, LSup + 1):
        print("Números no intervalo: ", i)