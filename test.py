import random
import clases

''' identificacion=diccionario[identificacion]
    horas_atencion=diccionario[horas_atencion]
    cantidad_intervalos=diccionario[cantidad_intervalos]
    total_clientes=diccionario[total_clientes]
    distribuciones=diccionario[distribuciones]
    cantidad_cajas_abiertas_cada_intervalo=diccionario[cantidad_cajas_abiertas_cada_intervalo]
    minimo_productos=diccionario[minimo_productos]
    maximo_productos=diccionario[maximo_productos]
    promedio_seleccion=diccionario[promedio_seleccion]
    promedio_marcado=diccionario[promedio_marcado]
    promedio_pago=diccionario[promedio_pago]'''
    
identificacion='Hola esto es una descripcion'
horas_atencion=1
cantidad_intervalos=10
total_clientes=100
distribuciones=[10,10,10,10,10,10,10,10,10,10]
cantidad_cajas_abiertas_cada_intervalo=[3,4,5,6,7,4,3,2,4,5]
minimo_productos=5
maximo_productos=15
promedio_seleccion=15
promedio_marcado=3
promedio_pago=40
print(identificacion)
print('\n')
#----------------------------------------------------------------------------------------
#intervalos - (cantidad clientes,segundos,cajas abiertas) EN CADA INTERVALO   ejemplo 1:(3,300)
intervalos=dict()
for i in range(cantidad_intervalos):
    clientes_intervalo=round((distribuciones[i]/100)*total_clientes)
    tiempo_intervalo=int((horas_atencion*60/10)*60)
    cajas_abiertas=cantidad_cajas_abiertas_cada_intervalo[i]
    t=clientes_intervalo,tiempo_intervalo,cajas_abiertas
    intervalos[i+1]=t
#-----------------------------------------------------------------------------------------    
#clientes - (cantidad de productos,tiempo_antes_de_la_caja) DE CADA CLIENTE 
clientes_datos=dict()
for i in range(total_clientes):
    random.seed()
    cantidad_productos=random.randint(minimo_productos,maximo_productos)
    tiempo_antes_de_la_caja=(1)#cantidad_productos*promedio_seleccion)
    t=cantidad_productos,tiempo_antes_de_la_caja
    clientes_datos[i+1]=t


#lista de los clientes(objetos)
clientes=[]
for i in range(total_clientes):
    c=clases.Cliente(clientes_datos[i+1][0],clientes_datos[i+1][1],1)#promedio_marcado*clientes_datos[i+1][0]+promedio_pago)
    clientes.append(c)

#--------------------------------------------------------------------------------------------
cajas_pendientes=[]
tiempo_total=0 # PRIMER REQUERIMIENTO B

for i in range(len(intervalos)): #Se repite el proceso de simulación por cada intervalo 
    clientes_en_el_intervalo=[] #lista de objetos
    cajas_abiertas_en_el_intervalo=[] #lista de objetos
    total_productos_despachados=0
#----------------------------------------------------------------------------------------------------------------------------------------------
    for numero in reversed(range(intervalos[i+1][0])): #Se llena la lista de clientes en el intervalo tomando clientes de la lista total de clientes
        clientes_en_el_intervalo.append(clientes[numero])
        clientes.pop()

    for n in range(intervalos[i+1][2]):#Se generan las cajas abiertas con sus respectivas colas vacias
        cola_objeto=clases.Cola()
        caja_objeto=clases.Caja(cola_objeto)
        cajas_abiertas_en_el_intervalo.append(caja_objeto)

    #print(len(clientes_en_el_intervalo))
#-------------------------------------------------------------------------------------------------------------------------------------------------
    cantidad_clientes_ingresados=len(clientes_en_el_intervalo) #SEGUNDO REQUERIMIENTO B
    tiempo=intervalos[i+1][1] #variable que guarda el tiempo que va a durar el intervalo actual
    tiempo_total+=tiempo/60
    despachados=0 #TERCER REQUERIMIENTO B  
    promedio_de_productos_por_cliente_despachado=0 #CUARTO REQUERIMIENTO B
    promedio_clientes_en_espera=0 #QUINTO REQUERIMIENTO B 
    cola_mas_larga=0 #SEXTO REQUERIMIENTO B
    clientes_en_espera=0
    total_cajas=len(cajas_abiertas_en_el_intervalo)+len(cajas_pendientes)
    for segundos in range(1,tiempo+1): #Empieza a correr el tiempo
        #print(segundos)
       # print(len(clientes_en_el_intervalo))
        #print("-------")
        '''contador=0
        contador_clientes=0
        for numero_caja in range(len(cajas_abiertas_en_el_intervalo)):
            if cajas_abiertas_en_el_intervalo[numero_caja].cola.Largo()>0:
                contador+=1
        for cliente in clientes_en_el_intervalo:
            if cliente.tiempo_en_caja>0:
                contador_clientes+=1
                
        if contador_clientes==0 and contador==0:
            break'''

        
        ''' if len(cajas_pendientes)>0: #si hay cajas pendientes, estas funcionan aparte de las que se abren en el intervalo 
            for numero in range(len(cajas_pendientes)):
                    
                if cajas_pendientes[numero].cola.Largo()>cola_mas_larga:
                    cola_mas_larga=cajas_pendientes[numero].cola.Largo()
                        
                if cajas_pendientes[numero].cola.primero!=None and cajas_pendientes[numero].cola.primero.tiempo_en_caja>0:
                    cajas_pendientes[numero].cola.primero.tiempo_en_caja-=1
                        
                elif cajas_pendientes[numero].cola.primero!=None and cajas_pendientes[numero].cola.primero.tiempo_en_caja==0:
                    cajas_pendientes[numero].cola.Desencolar()
                    despachados+=1

                if cajas_pendientes[numero].cola.Largo()>1:
                    clientes_en_espera+=cajas_pendientes[numero].cola.Largo()-1

                if cajas_pendientes[numero].cola.Largo()==0:
                    del cajas_pendientes[numero]'''
                
           
        for cliente in clientes_en_el_intervalo:   #quitarles un segundo a los que no estan encolados y al que esta primero en la fila 
            menor_cola=1000
            identificador_caja_menor_cola=1000
            if cliente.tiempo_antes_de_caja>0: #Esta seleccionando productos
                #print("D")
                cliente.tiempo_antes_de_caja-=1
                
            elif cliente.tiempo_antes_de_caja==0 and cliente.encolado==False: #No ha sido encolado y ya selecciono los productos
                for numero_caja in range(len(cajas_abiertas_en_el_intervalo)):
                    
                    if cajas_abiertas_en_el_intervalo[numero_caja].cola.getVacio()==True:
                        cajas_abiertas_en_el_intervalo[numero_caja].cola.Encolar(cliente)
                        cliente.encolado=True
                        clientes_en_espera+=1
                        break

                    else:
                        if cajas_abiertas_en_el_intervalo[numero_caja].cola.Largo()<menor_cola:
                            #print(len(cajas_abiertas_en_el_intervalo))
                            #print("chaoooo")
                            menor_cola=cajas_abiertas_en_el_intervalo[numero_caja].cola.Largo()
                            identificador_caja_menor_cola=numero_caja
                
                if cliente.encolado==False:
                    cajas_abiertas_en_el_intervalo[identificador_caja_menor_cola].cola.Encolar(cliente)
                    clientes_en_espera+=1
                    cliente.encolado=True
                    

            elif cliente.tiempo_en_caja>0 and cliente.encolado==True: #Esta pagando o estan pasando sus productos aún, se busca si es el primero de alguna caja
                for caja in cajas_abiertas_en_el_intervalo:
                    if caja.cola.primero==cliente:
                        cliente.tiempo_en_caja-=1
                
                '''es_el_primero=False
                for caja in cajas_abiertas_en_el_intervalo:
                    if caja.cola.primero==cliente:
                        es_el_primero=True
                if es_el_primero==True:
                    cliente.tiempo_en_caja-=1'''
                        
            elif cliente.tiempo_en_caja==0: #Ya pagó, se despacha
                #print("HOllaaaa")
                clientes_copia=clientes_en_el_intervalo
                for caja in cajas_abiertas_en_el_intervalo:
                    if caja.cola.primero==cliente:
                        caja.cola.Desencolar()
                        total_productos_despachados+=cliente.cantidad_productos
                        despachados+=1
                #for i in range(len(clientes_en_el_intervalo)):
                #print(clientes_en_el_intervalo[0])
                #if clientes_en_el_intervalo[i]==cliente:
                del clientes_en_el_intervalo[0]
               # print("clienteeee")
                
                        
        for caja in cajas_abiertas_en_el_intervalo:#Se busca la caja más larga hasta el momento
            #print(caja.cola.Largo())
            if caja.cola.Largo()>cola_mas_larga:
                cola_mas_larga=caja.cola.Largo()
                

        for caja in cajas_abiertas_en_el_intervalo:#Se agregan los clientes en espera
            if caja.cola.Largo()>1:
                clientes_en_espera+=caja.cola.Largo()-1

 
       
    for i in range(len(cajas_pendientes)): #se eliminan las cajas pendientes del intervalo anterior 
        del cajas_pendientes[0]

    for caja in cajas_abiertas_en_el_intervalo: #Se guardan las cajas que no alcanzaron a cerrar porque aun hay clientes
        if caja.cola.Largo()>0:
            cajas_pendientes.append(caja)
    if despachados!=0:
        promedio_de_productos_por_cliente_despachado+=total_productos_despachados/despachados
    
    promedio_clientes_en_espera=clientes_en_espera/total_cajas
    print('Datos para el intervalo '+str(i+1))
    print('\n')
    print('La cantidad de clientes ingresados es: '+str(cantidad_clientes_ingresados))
    print('\n')
    print('La cantidad de clientes despachados es: '+str(despachados))
    print('\n')
    print('El promedio de productos por cliente despachado es: '+str(int(promedio_de_productos_por_cliente_despachado)))
    print('\n')
    print('El promedio de clientes en espera en colas de caja es: '+str(int(promedio_clientes_en_espera)))
    print('\n')
    print('La longitud maxima de cola de espera en caja fue de: '+str(cola_mas_larga))
    print('\n')
    print('--------------------------------------------------')
if cajas_pendientes: #si es que aun quedan clientes despues del ultimo intervalo
    cantidad_clientes_ingresados=len(cajas_pendientes)
    despachados=0
    productos_despachados=0
    promedio_de_productos_por_cliente_despachado=0
    promedio_clientes_en_espera=0
    clientes_en_espera=0
    cola_mas_larga=0
    tiempo=0
    while (len(cajas_pendientes)>0):
        for numero in range(len(cajas_pendientes)):

                
                
            if cajas_pendientes[numero].cola.Largo()>cola_mas_larga:
                cola_mas_larga=cajas_pendientes[numero].cola.Largo()
                        
            if cajas_pendientes[numero].cola.primero.tiempo_en_caja>0:
                cajas_pendientes[numero].cola.primero.tiempo_en_caja-=1
                        
            elif cajas_pendientes[numero].cola.primero.tiempo_en_caja==0:
                productos_despachados+=cajas_pendientes[numero].cola.primero.cantidad_productos
                cajas_pendientes[numero].cola.Desencolar()
                despachados+=1
                        
            if cajas_pendientes[numero].cola.Largo()==0:
                del cajas_pendientes[numero]
                    
            clientes_en_espera+=cajas_pendientes[numero].cola.largo()-1
                
        tiempo+=1
    tiempo_total+=tiempo/60
    promedio_de_productos_por_cliente_despachado+=productos_despachados/despachados
    promedio_clientes_en_espera=int(clientes_en_espera/len(cajas_pendientes))
        
print('El tiempo total simulado en minutos es: '+str(tiempo_total))





    
'''tiempo=intervalos[i+1][1]
    print(tiempo)
    for t in range(tiempo):
        for cliente in clientes_en_el_intervalo:
            menor_cola=10000
            id_menor_caja=0
            if cliente.tiempo_antes_de_caja==0 and cliente.encolado==False:
                for id_caja in range(len(cajas_abiertas_en_el_intervalo)):'''



   
