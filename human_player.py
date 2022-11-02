from player import Player
from rules import Rules

class HumanPlayer(Player):
    def __init__(self, rules: Rules) -> None:
        super().__init__(rules)
        
    def do_turn(self, coins: int = -1) -> int:
        while True:
            try:
                take = int(input('How many coins would you like to take?: '))
                if take in range(self._rules.min_take, self._rules.max_take + 1):
                    return take
                raise ValueError
            except ValueError:
                print(f'Please enter a valid number between {self._rules.min_take} and {self._rules.max_take}.')
