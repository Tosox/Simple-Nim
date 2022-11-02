from player_manager import PlayerManager
from computer_player import ComputerPlayer
from human_player import HumanPlayer
from player import Player
from rules import Rules

class GameOf21(object):
    def __init__(self, rules: Rules = Rules()) -> None:
        self.__player_manager = PlayerManager()
        self.__rules = rules

    def run(self) -> None:
        self.__player_manager.add_player(ComputerPlayer(self.__rules))
        self.__player_manager.add_player(ComputerPlayer(self.__rules))
        self.__player_manager.randomize_player()
        coins = self.__rules.coins
        
        while (coins > 0):
            self.__print_game(coins, self.__player_manager.get_current())
            
            coins -= self.__player_manager.get_current().do_turn(coins)
            if coins <= 0:
                print(f'Player {self.__player_manager.get_current()} wins!')
            
            self.__player_manager.next()

    def __print_game(self, coins: int, player: Player) -> None:
        print('================================================')
        print(f'Total coins: {coins} | Player: {player}')
        

if __name__ == '__main__':
    game = GameOf21()
    game.run()
    