class Cliente(object):
    #Constructor y atributos
    def __init__(self,cantidad_productos,tiempo_antes_de_caja,tiempo_en_caja, id, atendido):
        self.cantidad_productos=cantidad_productos
        self.tiempo_antes_de_caja=tiempo_antes_de_caja
        self.tiempo_en_caja=tiempo_en_caja
        self.Patras=None
        self.atendido=atendido
        self.id = id


class Caja(object):
    def __init__(self,cola, ide):
        self.cola=cola
        self.ocupada = False
        self.pagando = None
        self.minimo = False
        self.identificador = ide
    

