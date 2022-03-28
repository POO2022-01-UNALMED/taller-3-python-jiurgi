class TV:
    
    _numTV=0
    def __init__(self, marca, estado):
        self._marca= marca
        self.canal= 1
        self._precio= 500
        self.estado= estado
        self.volumen=1
        self._numTV+=1
        
        
        
    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca  
        
        
    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if self._estado and canal >= 1 and canal <= 120:
            self._canal = canal  
        
    def getControl(self):
        return self._control   
    
    def setControl(self, control):
        self._control = control
        
    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio  
        
    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado    
    
    def setVolumen(self, volumen):
        if self._estado  and volumen >= 0 and volumen <= 7:
            self._volumen = volumen
  
    
    @classmethod
    def setNumTV(cls, numTV):
        TV._numTV = numTV
    
    # ----- OTROS -----
    def turnOn(self):
        self.estado = True

    def turnOff(self):
        self.estado = False

    def canalUp(self):
        if self.estado and self.canal < 120:
            self.canal += 1

    def canalDown(self):
        if self.estado and self.canal > 1:
            self.canal -= 1

    def volumenUp(self):
        if self.estado and self.volumen < 7:
            self.volumen += 1

    def volumenDown(self):
        if self.estado and self.volumen > 0:
            self.volumen -= 1