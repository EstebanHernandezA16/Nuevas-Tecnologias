

Nombre=''
Destino=1
#dependiendo del destino hay una variable para cada Total de personas por viaje
TotalPersonasGuajira=0
TotalNiñosGuajira=0
TotalAdultosGuajira=0
adultosGuajira=0
niñosGuajira=0
TotalNiñosGuajira=0
#TotalAdultos y TotalNiños
#TotalSubtotalGuajira
TotalPersonasCañon=0
TotalAdultosCañon=0
TotalNiñosCañon=0
niñosCañon=0
adultosCañon=0
#TotalAdultos y TotalNiños
#TotalSubtotalCañon
TotalPersonasLlanos=0
TotalAdultosLlanos=0
TotalNiñosLlanos=0
niñosLlanos=0
adultosLlanos=0

#TotalAdultos y TotalNiños
#TotalSubtotalLlanos
#Subtotal es sumatoria de todos los subtotales
subTotalGuajira=float(0)
subTotalCañon=float(0)
subTotalLlanos=float(0)
subTotal=float(0)
TotalAdultos = 0
TotalNiños= 0
TotalPersonas=0

respuesta=1
while respuesta==1:
    nombre = input('Ingrese su nombre: ')
    destino= int(input(f'{Nombre}, digite \n 1.para visitar la guajira \n 2. para visitar el Cañon del chicamocha \n 3. para visitar los Llanos Orientales \n '))
    while destino ==1:
        #logica de la guajira 
        adultosGuajira = int(input('¿Cuantos Adultos van a la guajira?'))
        niñosGuajira = int(input('¿Y cuantos niños?'))
        
        subTotalBaseGuajira= ((adultosGuajira*1450000)+(niñosGuajira*870000))
        subTotalGuajira= subTotalGuajira+subTotalBaseGuajira
        subTotal=subTotal+subTotalGuajira
        
        TotalNiñosGuajira= TotalNiñosGuajira+niñosGuajira
        TotalAdultosGuajira = TotalAdultosGuajira+adultosGuajira
        TotalPersonasGuajira = TotalPersonasGuajira + TotalAdultosGuajira+TotalNiñosGuajira
        
        TotalAdultos=TotalAdultos+TotalAdultosGuajira
        TotalNiños=TotalNiños+TotalNiñosGuajira  
        TotalPersonas = TotalPersonas + adultosGuajira+niñosGuajira
        print(f'{Nombre}, usted ha cotizado 1 viaje a la guajira con las siguientes caracteristicas: \n Destino: Guajira \n #Niños: {niñosGuajira}\n #Adultos: {adultosGuajira}\n Subtotal a pagar: {subTotalBaseGuajira}')     
        break
    while destino==2:
        #logica cañon 
        adultosCañon = int(input('¿Cuantos Adultos van al cañon de chicamocha?'))
        niñosCañon = int(input('¿Y cuantos niños?'))
        
        subTotalBaseCañon= ((adultosCañon*1600000)+(niñosCañon*960000))
        subTotalCañon= subTotalCañon+subTotalBaseCañon
        subTotal=subTotal+subTotalCañon
        
        TotalNiñosCañon= TotalNiñosCañon+niñosCañon
        TotalAdultosCañon = TotalAdultosCañon+adultosCañon
        TotalPersonasCañon = TotalPersonasCañon+TotalAdultosCañon+TotalNiñosCañon
        
        TotalAdultos=TotalAdultos+TotalAdultosCañon
        TotalNiños=TotalNiños+TotalNiñosCañon   
        TotalPersonas = TotalPersonas + adultosCañon+niñosCañon
        print(f'{Nombre}, usted ha cotizado 1 viaje para el cañon de chicamocha con las siguientes caracteristicas: \n Destino: Cañon de chicamocha \n #Niños: {niñosCañon}\n #Adultos: {adultosCañon}\n Subtotal a pagar: {subTotalBaseCañon}')  
        break
    while destino==3:
        #logica llanos
        adultosLlanos = int(input('¿Cuantos Adultos van a los llanos orientales?'))
        niñosLlanos = int(input('¿Y cuantos niños?'))
        
        subTotalBaseLlanos= ((adultosLlanos*1200000)+(niñosLlanos*720000))
        subTotalLlanos= subTotalLlanos+subTotalBaseLlanos
        subTotal=subTotal+subTotalLlanos
        
        TotalNiñosLlanos= TotalNiñosLlanos+niñosLlanos
        TotalAdultosLlanos = TotalAdultosLlanos+adultosLlanos
        TotalPersonasLlanos = TotalPersonasLlanos+TotalAdultosLlanos+TotalNiñosLlanos
        
        TotalAdultos=TotalAdultos+TotalAdultosLlanos
        TotalNiños=TotalNiños+TotalNiñosLlanos
        TotalPersonas = TotalPersonas + adultosLlanos+niñosLlanos
        print(f'{Nombre}, usted ha cotizado 1 viaje para los llanos orientales con las siguientes caracteristicas: \n Destino: llanos orientales \n #Niños: {niñosLlanos}\n #Adultos: {adultosLlanos}\n Subtotal a pagar: {subTotalBaseLlanos}')  
        
        break
    
    while destino!= 1 or destino!= 2 or destino!= 3:
       
        respuesta=1
        break
    respuesta= int(input('Quisiera cotizar otro viaje? 1.Si, 2.No'))
#imprimir todo
print(f'Dia laboral terminado, Cantidad de personas que viajan a la Guajira: {TotalPersonasGuajira},\n de los cuales {TotalAdultosGuajira} son adultos y {TotalNiñosGuajira} son niños,\n Cantidad de dinero cotizado para la Guajira: {subTotalGuajira},\n Cantidad de personas que viajan para el Cañon de chicamocha: {TotalPersonasCañon},\n de los cuales {TotalAdultosCañon} son adultos y {TotalNiñosCañon} son niños, \n Cantidad de dinero cotizado para el Cañon: {subTotalCañon}, \n Cantidad de personas que viajan a los llanos orientales: {TotalPersonasLlanos},\n de los cuales {TotalAdultosLlanos} son adultos y {TotalNiñosLlanos} son niños,\n Cantidad de dinero cotizado para los llanos: {subTotalLlanos}, \n Y por ultimo el total de personas fue de {TotalPersonas}, el total de dinero de todos los viajes fue de {subTotal} ')        