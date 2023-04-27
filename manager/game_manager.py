from custom.rules import Rules
from custom.rand_types import RandType
from players.player_types import PlayerType
from manager.player_manager import PlayerManager

class GameManager(object):
    def __init__(self, rules: Rules = Rules()) -> None:
        self.__player_manager = PlayerManager(rules)
        self.__rules = rules
        self.__coins = -1
        
    def initilize(self, players: tuple[PlayerType], randomize: RandType):           
        self.__player_manager.add_players(players)
        if randomize == RandType.RANDOM:
            self.__player_manager.randomize_turn()
        elif randomize == RandType.PLAYER2:
            self.__player_manager.next_turn()
        self.__coins = self.__rules.coins

    def run(self) -> None:
        if self.__player_manager.player_count() != 2:
            raise ValueError('Please call \'initialize()\' before running the game')
        
        while (self.__coins > 0):
            current_player = self.__player_manager.get_current_player()
            
            print('================================================')
            print(f'{current_player}\'s turn | Total coins: {self.__coins}')
            
            coins_take = current_player.do_turn(self.__coins)
            self.__coins -= coins_take
            
            print(f'-> Takes {coins_take} coins')
            print('================================================\n')
                    
            if self.__coins <= 0:
                print('================================================')
                winning_player = current_player if not self.__rules.misere else self.__player_manager.get_next_player()
                print(f'** {winning_player} wins! **')
                print('================================================')
            
            self.__player_manager.next_turn()
        
    