from rules import Rules
from player import Player
from player_types import PlayerType
from random_player import RandomPlayer
from human_player import HumanPlayer
from computer_player import ComputerPlayer
import random

class PlayerManager(object):
    def __init__(self, rules: Rules) -> None:
        self.__rules = rules
        self.__player_idx = 0
        self.__players = []
        
    def __type_to_player(self, player_type: PlayerType) -> Player:
        if player_type == PlayerType.RANDOM:
            return RandomPlayer(self.__rules)
        elif player_type == PlayerType.HUMAN:
            return HumanPlayer(self.__rules)
        elif player_type == PlayerType.COMPUTER:
            return ComputerPlayer(self.__rules)
        
    def add_players(self, players: tuple[PlayerType]) -> None:
        self.__players.append(players)
        
    def randomize_turn(self) -> None:
        self.__player_idx = random.randint(0, 1)
        
    def get_current_player(self) -> Player:
        return self.__players[self.__player_idx]
        
    def get_next_player(self) -> Player:
        index = (self.__player_idx + 1) % 2
        return self.__players[index]
    
    def next_turn(self) -> None:
        self.__player_idx = (self.__player_idx + 1) % 2
