"""
    @author jose.inestroza@unah.edu.hn
    @version 0.1.0 
    @date 2022/11/22
"""

from enum import Enum

class ServerState(Enum):
    BUSY = 1
    WAITING = 2

class EventType(Enum):
    ARRIVAL = 1
    DEPARTURE = 2