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
    for i in range(len(intervalos)):
        result = []
        resultados.append(result)
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
        def cajamenor(cajadispo):
            menor = cajasdispo[0]
            for s in range((len(cajasdispo))):
                if len(menor.cola) > len(cajasdispo[s].cola):
                    menor = cajasdispo[s]
            return menor




        cajasdispo = []
        for j in range(intervalos[k+1][0]):
            clientesd1.append(clientes2[0])
            clientes2.pop(0)

        for j in range(intervalos[k+1][2]):
            fila = []
            caja = clases.Caja(fila, str(j))

            cajasdispo.append(caja)

        for f in range(len(cajasdispo)):
            cajasdispo[f].pagando = clientesd1[0]

        atendidos = 0
        for tiempo in range(intervalos[k+1][1]):

            lenclient = len(clientesd1)

            for h in range(lenclient):
                if clientesd1[h].atendido == False:
                    if clientesd1[h].tiempo_antes_de_caja > 0:
                        clientesd1[h].tiempo_antes_de_caja -= 1
                    if clientesd1[h].tiempo_antes_de_caja == 0:

                        for s in range(len(cajasdispo)):
                            if cajasdispo[s].ocupada==False and clientesd1[h].atendido == False:
                                cajasdispo[s].pagando = clientesd1[h]
                                clientesd1[h].atendido = True

                                cajasdispo[s].ocupada=True


                        if clientesd1[h].atendido == False:
                            cajita = cajamenor(cajasdispo)
                            cajita.cola.append(clientesd1[h])
                            clientesd1[h].atendido = True


            for g in range(len(cajasdispo)):
                promediocaja.append(len(cajasdispo[g].cola))
                if colamax < len(cajasdispo[g].cola):
                    colamax = len(cajasdispo[g].cola)
                if cajasdispo[g].ocupada == True:
                    if cajasdispo[g].pagando.tiempo_en_caja > 0:
                        #print(cajasdispo[g].pagando.tiempo_en_caja,cajasdispo[g].pagando.id)
                        cajasdispo[g].pagando.tiempo_en_caja-=1
                    if cajasdispo[g].pagando.tiempo_en_caja == 0:
                        promprod.append(cajasdispo[g].pagando.cantidad_productos)
                        cajasdispo[g].pagando = None
                        cajasdispo[g].ocupada = False

                        atendidos+=1

                        if len(cajasdispo[g].cola)>0:
                            cajasdispo[g].pagando = cajasdispo[g].cola[0]
                            #print(cajasdispo[g].cola[0].id)
                            cajasdispo[g].cola.pop(0)
                            cajasdispo[g].ocupada = True


        promedio = 0
        for h in range(len(promprod)):
            promedio+=promprod[h]
        for s in range(len(promediocaja)):
            promediocola+=promediocaja[s]

        resultados[k].append(str(k+1))

        resultados[k].append(len(clientesd1))

        resultados[k].append(atendidos)

        resultados[k].append(str(int(promedio/intervalos[k+1][0])))

        resultados[k].append(str(round(int(promediocola)/(intervalos[k+1][2]*intervalos[k+1][1]))))

        resultados[k].append(str(colamax))
        resultados[k].append(horas_atencion*60)

        clientesd1 = []


    return resultados


