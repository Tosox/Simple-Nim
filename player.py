from rules import Rules
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, rules: Rules) -> None:
        self.PLAYER_TYPE = None
        self._rules = rules
        self.__name = ""
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
        
    def __str__(self) -> str:
        return str(self.idx + 1)
    
    @abstractmethod
    def do_turn(self, coins: int) -> int:
        pass
