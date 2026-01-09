num1=float(input("Insira um número inteiro:"))
num2=float(input("Insira outro número:"))
num3=float(input("Insira outro número:"))
num4=float(input("Insira outro número:"))
resto= num1 %2
resto2= num2 %2
resto3= num3 %2
resto4= num4 %2
if (resto==0)and num1>10:
    print(f"O número {num1} é par e de valor superior a 10")
elif (resto==0) and num1<10:
    print(f"O número {num1} é par e de valor inferior a 10")
elif (resto!=0) and num1>10:
    print(f"O número {num1} é impar e de valor superior a 10")
elif (resto!=0) and num1<10:
    print(f"O número {num1} é impar e de valor inferior a 10")

if (resto2==0)and num2>10:
    print(f"O número {num2} é par e de valor superior a 10")
elif (resto2==0) and num2<10:
    print(f"O número {num2} é par e de valor inferior a 10")
elif (resto2!=0) and num2>10:
    print(f"O número {num2} é impar e de valor superior a 10")
elif (resto2!=0) and num2<10:
    print(f"O número {num2} é impar e de valor inferior a 10")

if (resto3==0)and num3>10:
    print(f"O número {num3} é par e de valor superior a 10")
elif (resto3==0) and num3<10:
    print(f"O número {num3} é par e de valor inferior a 10")
elif (resto3!=0) and num3>10:
    print(f"O número {num3} é impar e de valor superior a 10")
elif (resto3!=0) and num3<10:
    print(f"O número {num3} é impar e de valor inferior a 10")
    
if (resto4==0)and num4>10:
    print(f"O número {num4} é par e de valor superior a 10")
elif (resto4==0) and num4<10:
    print(f"O número {num4} é par e de valor inferior a 10")
elif (resto4!=0) and num4>10:
    print(f"O número {num4} é impar e de valor superior a 10")
elif (resto4!=0) and num4<10:
    print(f"O número {num4} é impar e de valor inferior a 10")
    