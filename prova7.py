for i in range(1,1001):
    if (i%9==0 or i%7==0) and i%5!=0 and i%8!=0:
        print(i)
"""
v1 = 10
while ((v1>=1 and v1<=1000) and (v1%2==0) and(v1%4!=0)) 
    v1 = int(input("Introdueix l'operador:"))
    print(v1)
print("Has inserit un número menor o igual que 1, adéu!")

Docstring for prova7
v1 = 10
while(v1>=5 and v1<=10) or (v1>=15 and v1<=20) or (v1>=25 and v1<=30) and(v1!=6) and(v1!=16) and(v1!=26):
    v1 = int(input("Introdueix l'operador:"))
    print(v1)
print("Has inserit un número menor o igual que 5 o 15.")
v1 = int(input("Introdueix el primer operador"))
v2 = int(input("Introdueix el segon operador"))
r = v1 == v2
print(r)
r = v1 > v2
print(r)
r = v1 < v2
print(r)
r = v1 >= v2
print(r)
r = v1 <= v2
print(r)
v1 = int(input("Introdueix el primer operador"))
v2 = int(input("Introdueix el segon operador"))
r = v1 + v2 
print(r)
r = v1 - v2
print(r)
r = v1 * v2
print(r)
r = v1 // v2
print(r)
r = v1 / v2
print(r)
r = v1 % v2
print(r)
r = v1 ** v2
print(r)
r = v1 + (v2**2 / v1 - (v1%v2))
print(r)
"""