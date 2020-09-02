import json
import os, os.path
import glob


os.chdir(r'/Users/felipeignacioponcecanales/Felipe/WARM-uP-Tics/json')

datos = dict()
dias = 3
identificacion = 1
horas_atencion = 13
cantidad_intervalos = 2
total_clientes = 1200
distribuciones=[1,3,6,8,6,4,3,2]
cantidad_cajas_abiertas_cada_intervalo=30
minimo_productos=4
maximo_productos=5
promedio_seleccion=3
promedio_marcado = 4
promedio_pago = 3
datos = {
        "dias": dias,
        "identificacion" : identificacion,
        "horas_atencion" : horas_atencion,
        "cantidad_intervalos" : cantidad_intervalos,
        "total_clientes" : total_clientes,
        "distribuciones" : distribuciones,
        "cantidad_cajas_abiertas_cada_intervalo" : cantidad_cajas_abiertas_cada_intervalo,
        "minimo_productos" : minimo_productos,
        "maximo_productos" : maximo_productos,
        "promedio_seleccion" : promedio_seleccion,
        "promedio_marcado" : promedio_marcado,
        "promedio_pago" : promedio_pago
}

def exportjson(datos):

        dir = os.getcwd()+"/*.json"
        print(dir)
        Numero=len(glob.glob(str(dir)))
        print(Numero)
        Numero+=1

        with open('data'+str(Numero)+'.json','w') as outfile:
                json.dump(datos, outfile, indent=4)

exportjson(datos)


