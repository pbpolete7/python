def invertir(s):
    return s[::-1]

#Programa principal
cadena="Soc del Ramis"
s = list(cadena)
c = s.reverse()
p = "".join(c)
print("La inversa de {} és {}".format(cadena, invertir(cadena)))