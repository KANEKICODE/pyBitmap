from ctypes import resize;
from multiprocessing.dummy import Array;
import numpy as np;
from tokenize import String;

DESCRIPTION = """
Bitmap

Creado por: EdCoding
"""

class Bitmap(object):
    """
    Bitmap de valores booleanos
    """
    
    __size__ : tuple;
    __mask__ = np.zeros((8,8), dtype=bool);
    
    def __init__(self, size : tuple = (8,8)) -> None:
        """
        Crear un Bitmap
        """
        self.__size__ = size;
        self.__mask__ = np.resize(self.__mask__, (size));
    
    def __del__(self) -> None:
        """
        Destruir el BitMap
        """
        pass
    
    def setBit(self, pos : tuple, bitset : bool) -> None:
        """
        Establecer bit en la poscion dada
        """
        self.__mask__[pos] =  bitset;
        pass
    
    def setBitArray(self, a : Array) -> None:
        """
        Rellenar Bitmap con los valores del array dado
        """
        for y in range(0, len(a[0])):
            for x in range(0, len(a)):
                self.setBit((y,x), a[y][x]);
    
    def getBit(self, pos : tuple) -> bool:
        """
        Obtener bit en la poscion dada
        """
        return self.__mask__[pos];
    
    def getBitCount(self) -> int:
        """
        Obtener cantidad de bits activos
        """
        c : int = 0;
        
        for y in range(0, self.__size__[0]):
            for x in range(0, self.__size__[0]):
                if self.getBit((y,x))  == True:
                    c += 1;
        
        return c;
    
    def getSize(self) -> tuple:
        """
        Obtener el tamaño del bitmap
        """
        return self.__size__;
    
    def empty(self) -> None:
        """
        vaciar la matriz del bitmap
        """
        for y in range(0, self.__size__[0]):
            for x in range(0, self.__size__[0]):
                if self.getBit((y,x)) == True:
                    self.setBit((y,x), False);
        pass 
    
    #def getMask(self) -> Array:
    #    """
    #    Obtener la mascara de bits
    #    """
    #    return self.__mask__;
    
    def toString(self) -> String:
        """
        Retorna el Bitmap en un String
        """
        st : String = "";
        
        for y in range(0, self.__size__[0]):
            for x in range(0, self.__size__[0]):
                 # ESTO PARA QUE SE ALINIEN EN EL STRING
                if self.getBit((y,x)) == True:
                    st += str(self.getBit((y,x))) + "  | "; # IMPRIME UN ESPACIO EXTRA DESPUES DEL "True" PARA ALINEAR AL "False"
                else:
                    st += str(self.getBit((y,x))) + " | ";
            st += "\n";
        
        return st;

