class Cliente(object):
    #Constructor y atributos
    def __init__(self,tiempo_pago,adelante,atras):
        self.__tiempo_pago=tiempo_pago
        self.__adelante=adelante
        self.__atras=atras
    #Metodos
    def getTiempo(self):
        return self.__tiempo_pago

    def setTiempo(self,tiempo_nuevo):
        self.__tiempo_pago=tiempo_nuevo
