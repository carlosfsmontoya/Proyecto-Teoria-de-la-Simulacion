"""
    @author javierflores@unah.hn
    @version 0.1.0 
    @date 2022/11/24

    ***
    *Esta clase fue hecha tomando como referencia una clase del profesor donde se lee un archivo, 
    en lugar de leer un archivo lo crea. 
    ***

"""
class FileGenerator:

    def __init__(self) -> None:
        """
        Constructor.
        """
        pass
   
    def fileGeneratorTSV(self, name: str="structuredData.tsv", __LAMDA: float=0.2, __MU: float=0.3, data: list=[]):
        """
        Método que genera un archivo .tsv


        @param name String, nombre del archivo (inluyendo la extensión).
        @param __LAMDA float, constante usada para determinar los tiempos de llegada.
        @para __MU float, constante usada para determinar los tiempos de salida.
        @param data list, lista con los datos que serán impresos en el archivo.

        *Los datos en el archivo de salida se separan con tabulados (\t).
        """

        #Se crea el archivo.
        f = open(name,"w+")

        #Se introduce la información de las contantes.
        f.write("__LAMDA \t __MU \n")
        f.write(f"{__LAMDA} \t {__MU} \n\n")

        #Se introduce la información de cada replicación.
        f.write("# Replication \t Delay Mean \n")
        for i in range(len(data)):
            f.write(f"{i+1} \t {data[i]} \n")

        #Se cierra el flujo.
        f.close()