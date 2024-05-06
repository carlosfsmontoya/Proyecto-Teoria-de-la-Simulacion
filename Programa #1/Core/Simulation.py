"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0 
    @date 2022/11/22
"""

import random, statistics
from Core.Server import Server
from Core.EventIDGenerator import EventIDGenerator
from Core.Event import ArrivalEvent, DepartureEvent
from Core.StatesAndTypes import EventType, ServerState
from Core.FileGenerator import FileGenerator

class Simulation:

    __LAMDA = 0.2
    __MU = 0.3
    __N = []

    __idGenerator = EventIDGenerator()

    def __init__(self, N:int=10000):
        self.__N = N

    def getNextArrivalEvent (self, clock:int) -> ArrivalEvent:
        event = ArrivalEvent(
            clock + random.expovariate(self.__LAMDA),
            self.__idGenerator.get()
        )

        return event

    def getNextDepartureEvent (self, clock:int) -> DepartureEvent:
        event = DepartureEvent(
            clock + random.expovariate(self.__MU),
            self.__idGenerator.get()
        )

        return event

    def __simulation(self, nCostumers:int, lastTime:float):

        departures, arrivals = [], []
        clock, count = lastTime, 0
        eventList, queue = [], []
        server = Server()

        #Se genera el primer evento y se calenderiza.
        eventList.append(self.getNextArrivalEvent(clock))

        #Se inicia la simulación y continua mientras existen eventos.
        while not len(eventList)==0:
            event = eventList.pop(0)
            clock = event.getClock()

            if event.getType() == EventType.ARRIVAL:

                queue.append(None) #Q+=1
                arrivals.append(clock)            

                if server.getState() == ServerState.WAITING:

                    server.changeToBusy()
                    eventList.append(self.getNextDepartureEvent(clock))

                count += 1

                if count < nCostumers:
                    eventList.append(self.getNextArrivalEvent(clock))

            elif event.getType() == EventType.DEPARTURE:

                queue.pop(0) #Q-=1
                departures.append(clock)

                if len(queue) == 0:

                    server.changeToFree()
                else:
                    server.changeToBusy()
                    eventList.append(self.getNextDepartureEvent(clock))

        return (departures, arrivals)

  
    def __results(self, samples:list=[]) -> None:
        
        #Instancia de la clase FileGenerator.
        fg = FileGenerator()

        #Se llama a la función para crear un archivo tsv incluyendo las muestras obtenidas.
        fg.fileGeneratorTSV("structuredData.tsv", self.__LAMDA, self.__MU, samples)


    def probability(self, probability:float, nActual:int) -> int:
        """
        Método que calcula la cantidad de clientes según una probabilidad

        @param probability float, probabilidad a obtener.
        @param nActual int, cantidad de clientes actual.

        @return nCostumers int, cantidad de clientes que cumplen con la probabilidad.
        """

        nCostumers = 0

        for fp in range(nActual):
            
            #Se obtiene el resultado de cuantos clientes cumplen con los porcentajes de ida o vuelta.
            if random.random() <= probability:
                nCostumers +=1

        #Retorna la cantidad de clientes que entran a la siguiente cola o regresan a la anterior.
        return nCostumers 


    def run(self, replications:int=50, numberOfQueues:int=10) -> None:

        #Muestras acumuladas según replicaciones
        samples = []

        #Diccionario que almacenará cada cola con sus arrival y departures.
        self.queues = {}

        #Variable auxiliar que servirá para almacenar/restablecer la cantidad de paquetes al inicio de cada replicación.
        aux = self.__N

        for i in range(replications):

            #Recolección de datos
            delays = []
            random.seed()

            #Se restaura la cantidad de clientes customers cada replicación.
            self.__N = aux
            
            #Iterador de las colas en el diccionario.
            actualQueue = 0

            #Ciclo que se moverá a través de todas las colas.
            while actualQueue < numberOfQueues:
                
                #Se prepara un arreglo para cada cola almacenada en el diccionario.
                self.queues[f"Queue {actualQueue}, Arrivals"] = []
                self.queues[f"Queue {actualQueue}, Departures"] = []

                #Se ejecuta la simulación,
                #enviando como parámetros la cantidad de clientes y el tiempo inicial (el tiempo será 0 cuando se inicia la cola).
                departures, arrivals = self.__simulation(self.__N, 0)

                #Se almacenan los tiempos de entradas y salidas para la cola actual.
                self.queues[f"Queue {actualQueue}, Arrivals"] = arrivals
                self.queues[f"Queue {actualQueue}, Departures"] = departures
                
                #Se calcula la cantidad declientes que fueron atendidos e irán a la siguiente cola según la probabilidad del 95%.
                nCustomers = self.probability(0.95, self.__N)
                
                #Si la cantidad de clientes que deciden ir a la siguiente cola es mayor a cero
                #y no se está en el último "puesto", los clientes irán a la siguiente cola.
                if nCustomers > 0 and actualQueue < numberOfQueues-1:
                    
                    #Se actualiza el número de clientes que se atenderán en la siguiente cola.
                    self.__N = nCustomers

                    #Existe la posibilidad del 1% de que un cliente después de entrar a la siguiente cola se retire.
                    if(random.random() <= 0.01 and self.__N > 0):
                        self.__N-=1
                    
                    #Una vez que el cliente vaya a la siguiente cola se calcula la cantidad de clientes
                    #que pueden regresar a la cola anterior según la probabilidad del 4%.
                    nCustomers = self.probability(0.04, self.__N)
                    
                    #Si la cantidad de clientes que deciden regresar a la cola anterior es mayor a cero
                    #y no se está en el primer "puesto", los clientes irán a la cola anterior.
                    if nCustomers > 0 and actualQueue > 0:
                        
                        #Se obtiene el tiempo de la última salida que obtuvo la cola anterior.
                        lastTime = self.queues[f"Queue {actualQueue-1}, Departures"][len(self.queues[f"Queue {actualQueue-1}, Departures"])-1]
                        
                        #Se ejecuta la simulación,
                        #enviando como parámetros la cantidad de clientes que regresan y el tiempo inicial
                        #(el tiempo será el último tiempo de departures que se obtuvo en la cola anterior).
                        departures, arrivals = self.__simulation(nCustomers, lastTime)
           
                        #Se almacenan los tiempos de entradas y salidas para la cola anterior.                        
                        self.queues[f"Queue {actualQueue-1}, Arrivals"] += arrivals
                        self.queues[f"Queue {actualQueue-1}, Departures"] += departures
                        
                        #Existe la posibilidad del 1% de que un cliente después de regresar a la cola anterior se retire.
                        if(random.random() <= 0.01 and self.__N > 0):
                            self.__N-=1

                #Iterador del ciclo while.
                actualQueue+=1    
            
            #Una vez se obtienen los tiempos de arrivals y departures para la cantidad de colas
            #se procede a obtener los delays (retrasos).
            for iQueue in range(numberOfQueues):

                #Resultados estadísticos.
                delays += list(map(lambda x,y: x-y, self.queues[f"Queue {iQueue}, Departures"], self.queues[f"Queue {iQueue}, Arrivals"]))
            
            #Se almacena la media de delay obtenida para cada replicación.
            samples.append(statistics.mean(delays))
       
        #Se imprimen los resultados estadísticos
        self.__results(samples)