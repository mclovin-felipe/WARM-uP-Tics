import random
import clases


def simulacion(horas, cantintervalos, totalclientes, distri, cajas,minproductos, maxproductos, promseleccion, prommarcado, prompago):

    horas_atencion = horas
    cantidad_intervalos = cantintervalos
    total_clientes = totalclientes
    distribuciones = distri
    cantidad_cajas_abiertas_cada_intervalo = cajas
    minimo_productos = minproductos
    maximo_productos = maxproductos
    promedio_seleccion = promseleccion
    promedio_marcado = prommarcado
    promedio_pago = prompago
    clientesd1 = []
    resultados = []
    print('\n')
    promcaja = []
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
    #inicializa lista para guardar los resultados
    for i in range(len(intervalos)):
        result = []
        resultados.append(result)
    #inicializa los clientes
    for i in range(total_clientes):
        random.seed()
        cantidad_productos=random.randint(minimo_productos,maximo_productos)
        tiempo_antes_de_la_caja=cantidad_productos*promedio_seleccion
        tiempo_en_caja = promedio_pago+promedio_marcado*cantidad_productos

        t=cantidad_productos,tiempo_antes_de_la_caja, tiempo_en_caja
        clientes_datos[i+1]=t

    clientes=[]
    for i in range(total_clientes):
        c=clases.Cliente(clientes_datos[i+1][0],clientes_datos[i+1][1],clientes_datos[i+1][2],i+1, False)#promedio_marcado*clientes_datos[i+1][0]+promedio_pago)
        clientes.append(c)

    #--------------------------------------------------------------------------------------------

    clientes2 = clientes
    for k in range(len(intervalos)):

        colamax = 0
        promprod = []
        promediocaja=[]
        promediocola = 0

    #----------------------------------------------------------------------------------------------------------------------------------------------





        cajasdispo = []
        for j in range(intervalos[k+1][0]):
            clientesd1.append(clientes2[0])
            clientes2.pop(0)

        # funcion que devuelve la caja con menor cola
        def cajamenor(cajadispo):
            menor = cajasdispo[0]
            for s in range((len(cajasdispo))):
                if len(menor.cola) > len(cajasdispo[s].cola):
                    menor = cajasdispo[s]
            return menor
        #incializacion de cajas
        for j in range(intervalos[k+1][2]):
            fila = []
            caja = clases.Caja(fila, str(j))

            cajasdispo.append(caja)

        for f in range(len(cajasdispo)):
            cajasdispo[f].pagando = clientesd1[0]

        atendidos = 0
        #incio for de intervalos
        for tiempo in range(intervalos[k+1][1]):

            lenclient = len(clientesd1)
            #contempla dos casos, caso 1, si existe una casa vacia, caso 2, debe pasar el cliente a una cola
            for h in range(lenclient):
                #revisa elatributo atendido, en caso de ser FALSO, revisa si este aun le queda tiempo de seleccion de productos
                #en tal caso, se le resta 1 segundo
                if clientesd1[h].atendido == False:
                    if clientesd1[h].tiempo_antes_de_caja > 0:
                        clientesd1[h].tiempo_antes_de_caja -= 1
                    #se revisa si el tiempo antes de caja es 0, si es as
                    if clientesd1[h].tiempo_antes_de_caja == 0:
                        #se recorren las cajas correspondientes al intervalo
                        for s in range(len(cajasdispo)):
                            #se verifica si la caja esta ocupada, y si el cliente esta atendido, primero se revisa si hay una caja sin cola
                            if cajasdispo[s].ocupada==False and clientesd1[h].atendido == False:
                                cajasdispo[s].pagando = clientesd1[h]
                                clientesd1[h].atendido = True

                                cajasdispo[s].ocupada=True

                        #en caso de que las cajas esten ocupadas, se procede a inlcuir al cliente en alguna cola, buscando la caja con la menor cola
                        #esto gracias a la funcion cajamenor
                        if clientesd1[h].atendido == False:
                            cajita = cajamenor(cajasdispo)
                            cajita.cola.append(clientesd1[h])
                            clientesd1[h].atendido = True

            #manejo de los clientes en las cajas
            #se recorren las cajas disonibles
            for g in range(len(cajasdispo)):
                if len(cajasdispo[g].cola) != 0:
                    promediocaja.append(len(cajasdispo[g].cola))
                #Se guardaen una varibale la cola con mayor tamaño, se revisa constantemente
                if colamax < len(cajasdispo[g].cola):
                    colamax = len(cajasdispo[g].cola)
                #con el atributo ocupada, podremos saber si la caja esta con un cliente o no
                #si esta ocupada, procedera a descontar 1 segundo al tiempo del cliente en caja
                if cajasdispo[g].ocupada == True:
                    if cajasdispo[g].pagando.tiempo_en_caja > 0:
                        #print(cajasdispo[g].pagando.tiempo_en_caja,cajasdispo[g].pagando.id)
                        cajasdispo[g].pagando.tiempo_en_caja-=1
                    #en caso de que el tiempo en caja sea  0
                    if cajasdispo[g].pagando.tiempo_en_caja == 0:
                        #esto significa que el cliente acabo su compra, por lo tanto se procede a sacar el cliente del atributo de caja, pagando, que guarda un cliente
                        #y se cambia su estado de ocupada a False
                        promprod.append(cajasdispo[g].pagando.cantidad_productos)
                        cajasdispo[g].pagando = None
                        cajasdispo[g].ocupada = False
                        #sumamos 1 paara el contador de atendidos
                        atendidos+=1
                        #se procede a verificar la cola y se pasa el primero de la lista a la caja
                        if len(cajasdispo[g].cola)>0:
                            cajasdispo[g].pagando = cajasdispo[g].cola[0]
                            cajasdispo[g].cola.pop(0)
                            cajasdispo[g].ocupada = True


        promedio = 0
        #calculo de los promedios pedidos
        for h in range(len(promprod)):
            promedio+=promprod[h]
        promediocola = 0
        for s in range(len(promediocaja)):
            promediocola+=promediocaja[s]
        #resultados

        resultados[k].append(str(k+1))

        resultados[k].append(len(clientesd1))

        resultados[k].append(atendidos)
        if len(promprod) == 0:
            resultados[k].append("0")
        else:
            resultados[k].append(str(int(promedio/atendidos)))
        if len(promediocaja) == 0:
            resultados[k].append("0")
        else:
            resultados[k].append(str(round(int(promediocola)/len(promediocaja))))

        resultados[k].append(str(colamax))
        resultados[k].append(horas_atencion*60)

        clientesd1 = []


    return resultados
result = simulacion(15, 10,100,[10,10,10,10,10,10,10,10,10,10], [2,5,5,1,1,1,1,1,1,1],1,1,1000,1,1)
#print(result)

