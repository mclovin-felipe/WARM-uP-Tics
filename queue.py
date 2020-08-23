class queue(objeto):
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def isEmpty(self):
        return self.head == None

    def InsertarFinal(self, value):
        if(self.isEmpty()):
            self.head = clientes(value, None)
            self.tail = clientes(value, None)
        else:
            temp = self.head
            while(temp != None):
                if(temp.next == None):
                    temp.next = clientes(value, None)
                    self.tail = temp.next
                    return
                temp = temp.next
    def EliminarInicio(self):
        if(self.isEmpty()):
            return
        elif(self.head.next == None):
            self.head = None
        else:
            aux = self.head
            self.head = aux.next
            aux = None