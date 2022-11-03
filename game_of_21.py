from manager.game_manager import GameManager as GameOf21
from players.player_types import PlayerType

if __name__ == '__main__':    
    game = GameOf21()
    game.initilize((PlayerType.PLAYER, PlayerType.COMPUTER), True)
    game.run()
