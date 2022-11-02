from rules import Rules
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, rules: Rules) -> None:
        self._rules = rules
        self.__idx = 0
        
    @property
    def idx(self):
        return self.__idx
    
    @idx.setter
    def idx(self, index: int):
        self.__idx = index
        
    def __str__(self) -> str:
        return str(self.idx + 1)
    
    @abstractmethod
    def do_turn(self, coins: int) -> int:
        pass
