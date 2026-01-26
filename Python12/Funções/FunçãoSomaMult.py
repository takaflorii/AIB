def adicao(a1, a2):
    print("Adicionando ", a2, "a ", a1, "temos ", a1+a2)
    
def mult(m1,m2):
    print("Multiplicando ", m1, "por ", m2, "temos ", m1*m2)   

while True:   
    n1=float(input("Digite um número\n"))
    n2=float(input("Digite outro número\n"))

    op=input("Que operação deseja fazer?\nA -> Adição\nM > Multiplicação\n")

    if op == 'A':
        adicao(n1,n2)
    
    if op == 'M':
        mult(n1,n2)
    
    if op !='A' and op!='M':
        print("Operação inválida")
    
    continuar = input("\nDeseja fazer outra operação? (s/n): \n").lower()
    if continuar != 's':
        print("Programa encerrado. Até logo!")
        break