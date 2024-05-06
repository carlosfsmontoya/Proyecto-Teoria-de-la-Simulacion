"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0 
    @date 2022/11/22
"""

from Core.StatesAndTypes import EventType

class Event:

    __type = None
    __clock = 0
    __id = -1

    def __init__(self, type:EventType, clock:int, id:int):
        self.__type = type
        self.__clock = clock
        self.__id = id
        pass

    def getType(self) -> EventType:
        return self.__type

    def getClock(self) -> int:
        return self.__clock

    def getId(self) -> int:
        return self.__id

class ArrivalEvent(Event):

    def __init__(self, clock:int, id:int):
        super().__init__(EventType.ARRIVAL, clock, id)

class DepartureEvent(Event):

    def __init__(self, clock:int, id:int):
        super().__init__(EventType.DEPARTURE, clock, id)