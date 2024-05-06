"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0 
    @date 2022/11/22
"""

from Core.StatesAndTypes import ServerState

class Server:

    __state = ServerState.WAITING

    def __init__(self):
        pass

    def getState(self) -> ServerState:
        return self.__state

    def changeToBusy(self) -> None:
        self.__state = ServerState.BUSY

    def changeToFree(self) -> None:
        self.__state = ServerState.WAITING