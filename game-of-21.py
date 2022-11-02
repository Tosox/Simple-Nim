from player_manager import PlayerManager
from player_types import PlayerType
from rules import Rules

class GameOf21(object):
    def __init__(self, rules: Rules = Rules()) -> None:
        self.__player_manager = PlayerManager()
        self.__rules = rules
        self.__coins = -1
        
    def initilize(self, players: tuple[PlayerType], randomize: bool = True):
        self.__player_manager.add_players(players)
        if randomize:
            self.__player_manager.randomize_turn()
        self.__coins = self.__rules.coins

    def run(self) -> None:
        while (self.__coins > 0):
            current_player = self.__player_manager.get_current_player()
            
            print('================================================')
            print(f'Total coins: {self.__coins} | Player: {current_player}')
            
            coins_take = current_player.do_turn(self.__coins)
            self.__coins -= coins_take
            
            print(f'-> Takes {coins_take} coins')
            print('================================================\n')
                    
            if self.__coins <= 0:
                print('================================================')
                print(f'** Player {current_player} wins! **')
                print('================================================')
            
            self.__player_manager.next_turn()
        

if __name__ == '__main__':
    game = GameOf21()
    game.initilize((PlayerType.RANDOM, PlayerType.RANDOM), True)
    game.run()
    