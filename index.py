class Super(object):
    def __init__(self, nclientes, h_atencion, periodos, distribucion, ncajas, cant_min, cant_max):
        self.nclientes = nclientes
        while(True):
            if(self.nclientes < 1):
                self.nclientes = int(input('Ingresa un numero correcto'))
            else:
                break
        
        self.h_atencion = h_atencion
        self.periodos = periodos
        while(True):
            if(self.periodos < 9):
                self.periodos = int(input('Ingresa un periodo correcto'))
            else:
                break
        
        self.distribucion = distribucion
        while(True):
            if(len(self.distribucion) < 9):
                self.distribucion = input('Ingresa una distribucion correcta')
          
            k = 0
            print(self.distribucion)
            for x in self.distribucion:
                k += int(x)
                print(k)
            
            if(k != 100):
                input_distribucion = 0
                input_distribucion = input('Ingresa una distribucion correcta')
                self.distribucion = input_distribucion.split()
                print(self.distribucion)
                print(input_distribucion)
            else:
                break
        
        self.ncajas = ncajas
        while(True):
            if(self.ncajas < 1):
                self.ncajas = int(input('Ingresa un numero correcto de cajas'))
            else:
                break
        self.cant_min = cant_min
        while(True):
            if(self.cant_min < 1):
                self.cant_min = int(input('Ingresa un numero correcto de cajas'))
            else:
                break
        self.cant_max = cant_max
        while(True):
            if(self.cant_max < 1):
                self.cant_max = int(input('Ingresa un numero correcto de cajas'))
            else:
                break
        #---------------
        self.duracion = h_atencion*6

    def clienteshora(self,distribucion, nclientes):
        c_hora = []
        i=0
        while i< len(self.distribucion):
            c_hora.append( self.distribucion[i]*nclientes*0.01)
            i+=1
        return c_hora



p1 = Super(122, 10, 10, [ 5, 7, 9, 11, 14, 14, 9, 7, 11, 13], 1, 1, 10)
print(p1.duracion)1
