Nombre = (input('Digite su nombre: '))
N1 = float(input('Ingrese la nota #1: '))
N2 = float(input('Ingrese la nota #2: '))
N3 = float(input('Ingrese la nota #3: '))
definitiva = (N1+N2+N3)/3
# print(Nombre+' su nota final es '+str((N1+N2+N3)/3))

print(f'{Nombre} su nota final es : {str((N1+N2+N3)/3)}')

# if ((N1+N2+N3)/3 <3.0):
#     print('Ha perdido')    
    
# else:
#     print('Ha ganado siuuuuuu')
    
# if(0<= definitiva >=2):
#     print('Problemas de atencion')
# elif(2< definitiva >=3):    
#     print('Puede recuperar')
# elif(3< definitiva >=4):
#     print('Ganaste')
# elif(4< definitiva >=4.6):
#     print('Eres genial')
# else:
#     print('Eres el mejor')     

if(definitiva>0 and definitiva<=2):
    print('Problemas de atencion')
elif(definitiva>2 and definitiva<3):    
    print('Puede recuperar')
elif(definitiva>=3 and definitiva<=4):
    print('Ganaste')
elif(definitiva>4 and definitiva<=4.6):
    print('Eres genial')
elif(definitiva>4.6 and definitiva<=5)    
    print('Eres el mejor') 
else:
    print('Ingresaste una nota mayor a 5, error')