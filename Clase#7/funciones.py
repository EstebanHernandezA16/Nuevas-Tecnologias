#declarar funcion
#funcion void sin parametros

def NombreFuncion():
    print('Hola')
    
def Saludar(nombre):
    print(f'Hola: {nombre}')    
    
def Sumar(n1,n2):
    return n1+n2

def ParametrosPorDefecto(edad="21"):
    return edad

def retornarVariosValores(n1,n2):
    return (n1*n2, n1/n2)
   
#funcion main como en java
if __name__ =="__main__":
    NombreFuncion()
    Saludar('Esteban')
    print(f'tienes {ParametrosPorDefecto()}, tu suma es : {Sumar(n2=5, n1=3)}, la multiplicacion es {retornarVariosValores(3,5)[0]} y tambien la division es {retornarVariosValores(3,5)[1]}')

    