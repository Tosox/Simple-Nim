import random
import time
from custom.rules import Rules
from players.player_types import PlayerType
from players.player import Player

class ComputerPlayer(Player):
    def __init__(self, rules: Rules) -> None:
        super().__init__(rules)
        self.PLAYER_TYPE = PlayerType.COMPUTER
            
    def do_turn(self, coins: int) -> int:
        # Give the computer time to think (visually)
        delay = (random.random() * 1.5) + 0.5
        time.sleep(delay)
        
        should_take = (coins - int(self._rules.misere)) % (self._rules.min_take + self._rules.max_take)
        
        if should_take not in range(self._rules.min_take, self._rules.max_take + 1):
            should_take = random.randint(self._rules.min_take, self._rules.max_take)
        
        return should_take
    