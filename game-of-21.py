from player_manager import PlayerManager
from computer_player import ComputerPlayer
from human_player import HumanPlayer
from random_player import RandomPlayer
from rules import Rules

class GameOf21(object):
    def __init__(self, rules: Rules = Rules()) -> None:
        self.__player_manager = PlayerManager()
        self.__rules = rules

    def run(self) -> None:
        self.__player_manager.add_player(RandomPlayer(self.__rules))
        self.__player_manager.add_player(RandomPlayer(self.__rules))
        self.__player_manager.randomize_turn()
        coins = self.__rules.coins
        
        while (coins > 0):
            current_player = self.__player_manager.get_current_player()
            
            print('================================================')
            print(f'Total coins: {coins} | Player: {current_player}')
            
            coins_take = current_player.do_turn(coins)
            coins -= coins_take
            
            print(f'-> Takes {coins_take} coins')
            print('================================================\n')
                    
            if coins <= 0:
                print('================================================')
                print(f'** Player {current_player} wins! **')
                print('================================================')
            
            self.__player_manager.next_turn()
        

if __name__ == '__main__':
    game = GameOf21()
    game.run()
    