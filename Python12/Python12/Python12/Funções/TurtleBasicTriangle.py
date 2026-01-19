from turtle import forward, left, done 

def triangulo (cor, lado, veloc):
    for i in range(100):
            forward(100)
            left(120)
            forward(100)
            left(120)
            forward(100)
            done()
            
triangulo("blue", 100, 5)