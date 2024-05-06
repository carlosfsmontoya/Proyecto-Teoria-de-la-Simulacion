"""
    @author javierflores@unah.hn
    @version 0.1.0 
    @date 2022/12/06
"""

class FileGenerator:


    def __init__(self) -> None:
        """
        Constructor.
        """
        pass
    
    #Método que genera un archivo TXT.
    def fileGeneratorTXT(self, name:str, data:list):
        """
        Método que genera un archivo .txt

        @param name String, nombre del archivo (inluyendo la extensión).
        @param data list, lista con los datos que serán impresos en el archivo.
        """
        
        f = open(name,"w+")
        f.write(data)
        f.close()