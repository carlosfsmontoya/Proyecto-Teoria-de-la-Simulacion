"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0 
    @date 2022/11/23
"""

class DataManager:
    
    __lamda = 0
    __mu = 0

    def __init__(self) -> None:
        pass

    def read(self, fileName:str="") -> list:

        if len(fileName) == 0:
            return None

        f = open(fileName, "r")

        content = f.read() 

        #Se eliminas los tabulados y saltos de línea.
        content = content.replace(" \t ", ",")
        content = content.replace(" \n", ",")

        content = content.split(",")

        #Se eliminan los encabezados __LAMDA, __MU 
        content.pop(0)
        content.pop(0)

        #Se eliminan los encabezados #Replication, Delay Mean 
        content.pop(2)
        content.pop(2)
       
        #Se obtienen las constantes __LAMDA y __MU del archivo.

        self.setLamda(float(content.pop(0)))
        self.setMu(float(content.pop(0)))

        #Se elima la columna de replicaciones, dejando solamente la columna Delay Mean.
        n = 0

        while n < len(content):

            content.pop(n)

            n+=1    
      
        return content

    def TSVToNumberList(self, dataList:list=[]) -> list:

        return list(map(lambda x: float(x), dataList))

    #Métodos mutadores de las variables.
    def setLamda(self, lamda) -> None:
        self.__lamda = lamda

    def setMu(self, mu) -> None:
        self.__mu = mu

    #Métodos accesores de las variables.
    def getLamda(self) -> float:
        return self.__lamda

    def getMu(self) -> float:
        return self.__mu

  