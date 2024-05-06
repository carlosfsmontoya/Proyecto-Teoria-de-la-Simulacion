"""
    @author javierflores@unah.hn
    @version 0.1.0 
    @date 2022/12/06
"""

from Core.DataManager import DataManager
from Core.Plot import Plot
from Core.Result import Result

#Instancia de la clase DataManager.
tsv = DataManager()

#Se lee el archivo structuredData.tsv y se prepara para ser usado.
structuredData = tsv.read("structuredData.tsv")

#Se extraen las variables lamda y mu de structuredData.tsv.
lamda = tsv.getLamda()
mu = tsv.getMu()

#Finalmente, se obtiene una lista con los Delay Mean,
samples = tsv.TSVToNumberList(structuredData)

#Instancia de la clase Result.
result = Result()

#Se imprimen los resultados.
result.results(lamda, mu, samples)

#Instancia de la clase Plot.
plt = Plot()

#Se grafican las muestras obtenidas.
plt.run(samples)

