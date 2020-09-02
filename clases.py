class Cliente(object):
    #Constructor y atributos
    def __init__(self,cantidad_productos,tiempo_antes_de_caja,tiempo_en_caja):
        self.cantidad_productos=cantidad_productos
        self.tiempo_antes_de_caja=tiempo_antes_de_caja
        self.tiempo_en_caja=tiempo_en_caja
        self.Patras=None
        self.encolado=False


class Caja(object):
    def __init__(self,cola):
        self.cola=cola
    

class Cola(object):
    def __init__(self):
        self.primero=None
        self.ultimo=None

    def getVacio(self):
        if(self.primero==None):
            return True
    def Largo(self):
        if self.getVacio()==True:
            return 0
        else:
            contador=0
            temporal=self.primero
            validar=True
            while(validar):
                contador+=1
                if temporal.Patras==None:
                    #print("aloha")
                    validar=False
                else:
                    temporal=temporal.Patras
            return contador
                
            
    def Encolar(self,cliente):
        if (self.getVacio()==True):
            self.primero=self.ultimo=cliente
        else:
            self.ultimo.Patras=cliente
            self.ultimo=cliente
        return True
    
    def Desencolar(self):
        if (self.getVacio()==True):
            return False
        elif(self.primero==self.ultimo):
            self.primero=self.ultimo=None
            return True
        
        else:
            temp=self.primero
            self.primero=self.primero.Patras
            temp=None
            return True

