while True:   
    print("\nDigite um número\n")
    a=float(input())
    print("Digite outro número\n")
    b=float(input())
    print("Que operação deseja fazer?\n")
    op=input()

    if op =='+':
            op_adicao=a+b
            print( "Adição -> ",a,"+" , b, "=" ,op_adicao)

    elif op == '-':
            op_subtracao=a-b
            print("Subtração -> ",a,"-", b, "=" , op_subtracao)

    elif op == '*':
            op_multiplicacao=a*b
            print ("Multiplícação ->" ,a,"X" ,b,"=" , op_multiplicacao)
    elif op == '/':
            op_divisao=a/b
            print( "Divisão -> ",a," / ",b,"=",op_divisao)
    elif op == '//':
            op_divisao_int=a//b
            print ( "Divisão inteira ->",a,"//",b,"=",op_divisao_int)

    elif op =='%':
            op_modulo_div=a%b
            print ("Módulo -> ",a,"%", b, "=" , op_modulo_div)

    elif op == '**':
            op_exponenciacao=a**b
            print ("Exponenciação ->" ,a, "**" , b,"=" , op_exponenciacao)
    
    continuar = input("\nDeseja fazer outra operação? (s/n): ").lower()
    if continuar != 's':
        print("Programa encerrado. Até logo!")
        break