class ProritiQ ():
    def __init__(self,large):
        self.lista=[None]
        
        self.large=large+1
        
        self.longitud=0
        
    
    
    def getLarge(self):
        return self.large
    
    def getNumber(self,p):
        return self.lista[p]
    
    
    def getLista(self):
        return self.lista
    
    
    def ObtenerPosicion(self,valor):
        iterdaor=0
        for i in self.lista :
            if i == valor :
                return iterdaor
            iterdaor+=1
        
        return "no se encontro el el valor "
    
    def obtenerHijoDerecho(self,nodo):
        
        
        try :
            var=(self.ObtenerPosicion(nodo)*2)+1
           
        except:
            return "no existe ese nodo " 

        
        try :
            return self.lista[var]
        except:
            return "no tiene hijo derecho "
        
        
    def obtenerHijoIzquierdo(self,nodo):
        
        
        try :
            var=(self.ObtenerPosicion(nodo)*2)
            
        except:
            return "no existe ese nodo " 
        

        
        try :
            return self.lista[var]
        except:
            return "no tiene hijo izquierdo "
        
        
    def obtenerPadre(self,valor):
        if self.ObtenerPosicion(valor)==1:
            return 0
        
        var=int(self.ObtenerPosicion(valor)/2)
        
        return self.lista[var]
        
        
    def Organizar(self,nodo):
        
        if self.obtenerPadre(nodo)==0:
            return
        #   este mayor que determina el orden de la lista de prioridad
        if self.obtenerPadre(nodo)  >  nodo :
  
            var2=self.obtenerPadre(nodo)

            var=self.ObtenerPosicion(nodo)
            
            self.lista[self.ObtenerPosicion(self.obtenerPadre(nodo))]=nodo
            
            self.lista[var]=var2
            
            self.Organizar(nodo)
        
    
    def mostrar(self):
        l=[]
        
        for i in self.lista:
            if i ==None:
                continue
            
            l.append(i)
            
        print(l)
       
        
        
    def add(self,nodo):
        if self.large==self.longitud+1:
            return print("ya no se pueden introducir mas numeros")
        
        if self.longitud==0:
            self.lista.append(nodo)
            self.longitud+=1
            return
        
        
        self.lista.append(nodo)
        
        self.longitud+=1

        self.Organizar(nodo)
        
        
        
    def eliminar(self):
        
        if self.longitud==0 :
            return print("no tinenes elementos en la cola de prioridad")
        
        
        if self.longitud==1:
            self.lista.pop(1)
            
            self.longitud-=1
            return
        
        var=self.obtenerHijoDerecho(self.lista[1])
        
        
        var2=self.obtenerHijoIzquierdo(self.lista[1])
        if self.longitud==2 :
            var2=0
            var=0
        
        self.lista.pop(1)
        
        if var2<var :
        
            self.lista[1]=var
            
            
            self.lista[2]=var2
        
        for i in self.getLista() :
            if i ==None:
                continue
            
            self.Organizar(i)
            
        self.longitud-=1
        
      

objeto=ProritiQ(10)

objeto.add(80)
objeto.add(4)
objeto.add(100)
objeto.add(2)
objeto.add(7)
objeto.add(22)
objeto.add(44)
objeto.add(68)
objeto.add(5)
objeto.add(1)

objeto.mostrar()





        
