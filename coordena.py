import math as mt
print ("CODIGO QUE TRANSFORMA COORDENADAS CARTESIANAS EN COORDENADAS POLARES")

r=float(input("Digite valor de r"))
theta=float(input("Digite el valor de teta:"))

x=r*mt.cos(theta)
y=r*mt.sin(theta)
print(x)
print(y)


print ("NAVE ESPACIAL")

xx=float(input("Digite a ubicacion en años luz: "))
v=float(input("Digite el valor de v en fraccion de c:"))

am=xx*9.461e15 #m
t=am/v #s
c=3e8 #m/s

print ("El tiempo que le toma a la nave espacial en llegar al planeta visto desde la tierra es: ")
print ("t=",t,"seg")

r=(mt.sqrt(1-((v**2)/(c)))**-1)
T=(t-((v*x)/c)) #s

print ("El tiempo que le toma a la nave espacial en llegar al plantea visto desde la nave es:")
print ("t=",T,"seg")

print ("SECUENCIA FIBONACCI HASTA 1000")

f1=1
f2=1
print(f1)
print(f2)
f3=f1+f2
print(f3)
while f3<1000:
	f1=f2
	f2=f3
	f3=f1+f2
	if f3>1000:
		break
	print(f3)   

