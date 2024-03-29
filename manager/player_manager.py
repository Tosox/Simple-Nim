import random
from custom.rules import Rules
from players.player import Player
from players.player_types import PlayerType
from players.random_player import RandomPlayer
from players.human_player import HumanPlayer
from players.computer_player import ComputerPlayer
from players.ai_player import AiPlayer

class PlayerManager:
    def __init__(self, rules: Rules) -> None:
        self.__rules = rules
        self.__player_idx = 0
        self.__players = ()
        
    def __type_to_player(self, player_type: PlayerType) -> Player:
        if player_type == PlayerType.RANDOM:
            return RandomPlayer(self.__rules)
        elif player_type == PlayerType.HUMAN:
            return HumanPlayer(self.__rules)
        elif player_type == PlayerType.COMPUTER:
            return ComputerPlayer(self.__rules)
        elif player_type == PlayerType.AI:
            return AiPlayer(self.__rules)
        
    def player_count(self) -> str:
        return len(self.__players)
        
    def add_players(self, players: tuple[PlayerType]) -> None:
        player1 = self.__type_to_player(players[0])
        player2 = self.__type_to_player(players[1])
        
        player1.name = player1.PLAYER_TYPE.name.capitalize()
        player2.name = player2.PLAYER_TYPE.name.capitalize()
        if player1.PLAYER_TYPE == player2.PLAYER_TYPE:
            player1.name += ' 1'
            player2.name += ' 2'
        
        self.__players = (player1, player2)
        
    def randomize_turn(self) -> None:
        self.__player_idx = random.randint(0, 1)
        
    def get_current_player(self) -> Player:
        return self.__players[self.__player_idx]
        
    def get_next_player(self) -> Player:
        index = (self.__player_idx + 1) % self.player_count()
        return self.__players[index]
    
    def next_turn(self) -> None:
        self.__player_idx = (self.__player_idx + 1) % self.player_count()
