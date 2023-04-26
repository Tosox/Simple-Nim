import sys

from manager.game_manager import GameManager as GameOf21
from players.player_types import PlayerType
from custom.utils import bcolors


def main(argv: list[str]) -> None:
    """
    Entry point

    Args:
        argv (list[str]): Program arguments
    """
    
    # Check if the syntax is valid
    argc = len(argv)
    if (argc != 5) and (argc != 7):
        print(f'{bcolors.FAIL}Error: please use the correct syntax: python game_of_21.py -p1 <player_type> -p2 <player_type> [Optional: --rand <int>]{bcolors.ENDC}')
        return
    
    # Get the player type of player 1
    p1_idx = argv.index('-p1') + 1
    p1 = argv[p1_idx]
    
    # Get the player type of player 2
    p2_idx = argv.index('-p2') + 1
    p2 = argv[p2_idx]
    
    # Get the optional input rand
    try:
        rand_idx = argv.index('--rand') + 1
        rand = argv[rand_idx]
    except ValueError:
        rand = 0
    
    game = GameOf21()
    game.initilize((PlayerType.PLAYER, PlayerType.COMPUTER), True)
    game.run()
    

if __name__ == '__main__':    
    main(sys.argv)
