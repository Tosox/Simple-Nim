from rules import Rules
from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, rules: Rules) -> None:
        self._rules = rules
        self.idx = 0
        
    @property
    def idx(self):
        return self.idx
    
    @idx.setter
    def idx(self, index: int):
        self.idx = index
        
    def __str__(self) -> str:
        return self.idx
    
    @abstractmethod
    def do_turn(self, coins: int) -> int:
        pass
