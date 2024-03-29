from abc import ABC, abstractmethod
from custom.rules import Rules
from players.player_types import PlayerType

class Player(ABC):
    def __init__(self, rules: Rules) -> None:
        self.PLAYER_TYPE = PlayerType.RANDOM
        self._rules = rules
        self.__name = ""
        
    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
        
    def __str__(self) -> str:
        return self.__name
    
    @abstractmethod
    def do_turn(self, coins: int) -> int:
        pass
