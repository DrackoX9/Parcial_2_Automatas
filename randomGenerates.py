
#Metodo cuadratico
def generateNumbersC( xn, m):
    
    for i in range(10):
        xn=(xn*(xn+1))%m
        print('X',i+1,' = ', xn)
def generateNumbersCM(xn):
    for i in range(10):
        cuadrado = xn*xn      #cuadrado
        cuadrado = str(xn)    #tranformar a cadena
        size=cuadrado.__sizeof__



print("Ingresse el valor de la semilla")
xn=int(input())
print("Ingrese el valor de m")
m=int(input())
generateNumbersC(xn,m)