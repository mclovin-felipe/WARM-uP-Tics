import json
import os, os.path
import glob






def exportjson(id,horas,cant_int, total, distri, cantcajas, minprod, maxprod, promselec,prommercad, prompago):
        datos = dict()

        datos = {
                "identificacion": id,
                "horas_atencion": horas,
                "cantidad_intervalos": cant_int,
                "total_clientes": total,
                "distribuciones": distri,
                "cantidad_cajas_abiertas_cada_intervalo": cantcajas,
                "minimo_productos": minprod,
                "maximo_productos": maxprod,
                "promedio_seleccion": promselec,
                "promedio_marcado": prommercad,
                "promedio_pago": prompago
        }
        dir = os.getcwd()+"/*.json"
        Numero=len(glob.glob(str(dir)))
        Numero+=1

        with open('data'+str(Numero)+'.json','w') as outfile:
                json.dump(datos, outfile, indent=4)





