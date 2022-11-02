from player_types import PlayerType
from player import Player
from rules import Rules
import random

class ComputerPlayer(Player):
    def __init__(self, rules: Rules) -> None:
        super().__init__(rules)
        self.PLAYER_TYPE = PlayerType.COMPUTER
            
    def do_turn(self, coins: int) -> int:
        should_take = (coins - int(self._rules.misere)) % (self._rules.min_take + self._rules.max_take)
        
        if should_take not in range(self._rules.min_take, self._rules.max_take + 1):
            should_take = random.randint(self._rules.min_take, self._rules.max_take)
        
        return should_take
    