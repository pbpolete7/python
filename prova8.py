#Llegir 2 nombres
#Imprimir tots els nombres entre el menor i el major
def ordenar(x, y):
    if x>y:
        return x, y
    elif y>x:
        return y, x
    else:
        return x, y
    
    #programa principal
v1 = int(input("Intro el 1r número: "))
v2 = int(input("Intro el 2n número: "))
v1, v2 = ordenar(v1, v2)
for e in range(v2, v1+1):
    print(e)

"""#Llegir 2 nombres
v1 = int(input("Intro el 1r número: "))
v2 = int(input("Intro el 2n número: "))
#Multiplicar-los i dividi-los per 2
r = (v1*v2) // 2
#Llavors imprimir del el número fins 0
for i in range(r, -1, -1):
    print(i)
v1 = int(input("Intro el 1r número:"))
v2 = int(input("Intro el 2n número:"))
r = v1*v2
if (r>=25 and r<=35) or (r>=105 and r<=125):
    print("A")
elif (r>=45 and r<=65) or (r>=145 and r<=165):
    print("B")
else:
    print("C")"""
