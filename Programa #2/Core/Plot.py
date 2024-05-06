"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0 
    @date 2022/10/05
"""

from matplotlib.pyplot import xlabel, ylabel, plot, savefig

class Plot:

    def __init__(self) -> None:
        pass

    def run(self, samples):

        xlabel('Replications', size=20)
        ylabel('Means', size=20)
        
        plot(samples)
        savefig('mean.jpg', format='jpeg', bbox_inches='tight')