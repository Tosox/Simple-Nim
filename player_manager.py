from player import Player
import random

class PlayerManager(object):
    def __init__(self) -> None:
        self.__player_idx = 0
        self.__players = []
        
    def get_player_count(self) -> int:
        return len(self.__players)
        
    def randomize_turn(self) -> None:
        highest_idx = self.get_player_count() - 1
        self.__player_idx = random.randint(0, highest_idx)
    
    def add_player(self, player: Player) -> None:
        player.idx = self.get_player_count()
        self.__players.append(player)
        
    def get_current_player(self) -> Player:
        return self.__players[self.__player_idx]
        
    def get_next_player(self) -> Player:
        player_count = self.get_player_count()
        index = (self.__player_idx + 1) % player_count
        return self.__players[index]
    
    def next_turn(self) -> None:
        player_count = self.get_player_count()
        self.__player_idx = (self.__player_idx + 1) % player_count
