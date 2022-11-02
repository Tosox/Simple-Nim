from player import Player
from rules import Rules
import random

class RandomPlayer(Player):
    def __init__(self, rules: Rules) -> None:
        super().__init__(rules)
        
    def do_turn(self, coins: int = -1) -> int:
        return random.randint(self._rules.min_take, self._rules.max_take)
