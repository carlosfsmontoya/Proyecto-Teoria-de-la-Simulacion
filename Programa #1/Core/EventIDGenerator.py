"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0 
    @date 2022/11/22
"""

class EventIDGenerator:

    __id = -1

    def __init__(self):
        pass

    def get(self) -> int:
        self.__id += 1
        return self.__id