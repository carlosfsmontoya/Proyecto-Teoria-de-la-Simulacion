"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0 
    @date 2022/10/05
"""

from Core.FileGenerator import FileGenerator 
import math
import statistics

class Result:

    def __init__(self) -> None:
        pass    

    def results(self, lamda:float, mu:float, samples:list=[]) -> None:

        sampleMean = statistics.mean(samples)
        sampleStandardDeviation = statistics.stdev(samples)
        t = 1.96

        #len(samples): el tamaño del arreglo de muestras y por tanto contiene la cantidad de replicaciones.
        ci1 = sampleMean - t * (sampleStandardDeviation / math.sqrt(len(samples)))
        ci2 = sampleMean + t * (sampleStandardDeviation / math.sqrt(len(samples)))

        results = f"""
Average Delay = {round(sampleMean, 2)}
Confidence Interval: ( {round(ci1, 2)}, {round(ci2,2)} )
Population Mean = {round(1 / (mu-lamda), 2)}
        """
        
        #Crear archivo txt de salida.
        fg = FileGenerator()
        fg.fileGeneratorTXT("output.txt", results)
    
    
