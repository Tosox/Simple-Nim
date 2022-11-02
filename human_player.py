from multiprocessing.sharedctypes import Value
from player import Player
from rules import Rules

class HumanPlayer(Player):
    def __init__(self, rules: Rules) -> None:
        super().__init__(rules)
        
    def do_turn(self, coins: int) -> int:
        while True:
            try:
                take = int(input('How many coins would you like to take?: '))
                if take in range(super()._rules.min_take, super()._rules.max_take):
                    return take
                raise ValueError
            except ValueError:
                pass
