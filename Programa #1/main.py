from Core.Simulation import Simulation

#Construye una instancia del simulador
sim = Simulation(N=6500)
        
#Se pretende que run() genere un resultado estadístico en pantalla
sim.run(replications=3650, numberOfQueues=20)