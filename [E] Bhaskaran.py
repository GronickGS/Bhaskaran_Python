import math
from unittest import result


def e2g(a,b,c):
    dis = (math.pow(b,2) - 4 * a * c)

    if a == 0:
        print("El valor de a debe ser diferente a 0")
    elif dis < 0:
        print("Solucion solo en numeros complejos")
    else:
        x1 = (-b + math.sqrt(dis)) / (2*a)
        x2 = (-b - math.sqrt(dis)) / (2*a)
        print(f"x1: {x1}, x2: {x2}")
#Programa principal
a = float(input("Ingrese valor de a: "))
b = float(input("Ingrese valor de b: "))
c = float(input("Ingrese valor de c: "))
resul = e2g(a,b,c)