from player import Player
from rules import Rules
import random

class ComputerPlayer(Player):
    def __init__(self, rules: Rules) -> None:
        super().__init__(rules)
            
    def do_turn(self, coins: int) -> int:
        should_take = (coins - int(self._rules.misere)) % (self._rules.min_take + self._rules.max_take)
        
        if should_take in range(self._rules.min_take, self._rules.max_take):
            print(f'Takes {should_take} coins')
            return should_take
        
        return random.randint(self._rules.min_take, self._rules.max_take)
    