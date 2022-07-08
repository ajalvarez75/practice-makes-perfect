class square():
    #size=0, if a value is not introduced, size take 0 as value by default.
    def __init__ (self,size=0):
        self.__size=size

    def area(self):
        a=self.__size*self.__size
        return a

    #getter, para obtener un atributo privado
    #los decoradores deben incluirse
    @property
    def size(self):
        return self.__size

    #setter, para cambiar un atributo privado
    @size.setter
    def size(self,size):
        if type(size)==int:
            self.__size=size
        else:
            print("Please introduce an integer number")

    def print(self):
        for i in range(1,self.size+1,1):
            print("#"*self.size)

#instancia=clase(parametro)
square1=square(80)
#square.size=20
#print(square.area())
square2=square(20)
print(square1.area())

#para cambiar el setter
square1.size="Hello"
print(square1.size)

square1.print()