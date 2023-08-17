# Ejemplo basico tabla de multiplicar

#for
# Numero = int(input('Ingrese un numero: '))
# for i in range(1,11):
    # print(f'{Numero} * {i} = {Numero*i}')
    
#while
# respuesta = 1

# while respuesta == 1:
#     respuesta = int(input('¿Desea continuar?\n 1. Si\n 2. No\n'))
#     while respuesta!=1 and respuesta!=2:
#         print('Digito no reconocido')
#         respuesta = int(input('¿Desea continuar?\n 1. Si\n 2. No\n'))
clave = '123'
for i in range(1,4):
    respuesta = input('Digite la clave')
    if(respuesta!=clave):
        print(f'Clave incorrecta, tiene {3-i} intentos más')
        if(i==3):
            print('Intentos agotados, bloqueado por 24 horas')
    else:
        print('Bienvenido')
        break    
    