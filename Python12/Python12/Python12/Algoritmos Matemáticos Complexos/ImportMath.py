from math import pi, pow

print("Qual a medida do raio?")
r=float(input())
prm=2*pi*r
area=pi*pow(r, 2)

print("O perímetro do círculo é ", prm, "u.a e a área é ", area, "u.a")
