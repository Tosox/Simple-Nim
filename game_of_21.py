import sys
from manager.game_manager import GameManager as GameOf21
from players.player_types import PlayerType
from custom.utils import bcolors
from custom.rand_types import RandType

def get_player_type(uinput: str) -> PlayerType:
    uinput = uinput.lower()
    if uinput == "player":
        return PlayerType.PLAYER
    elif uinput == "ai":
        return PlayerType.AI
    elif uinput == "computer":
        return PlayerType.COMPUTER
    elif uinput == "random":
        return PlayerType.RANDOM
    else:
        return -1

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
    
    # Check if syntax for player type 1 is valid
    try:
        p1_idx = argv.index('-p1') + 1
        p1 = argv[p1_idx]
    except ValueError:
        print(f'{bcolors.FAIL}Error: please use the correct syntax: python game_of_21.py -p1 <player_type> -p2 <player_type> [Optional: --rand <int>]{bcolors.ENDC}')
        return
        
    # Get player type for player 1
    p1_type = get_player_type(p1)
    if p1_type == -1:
        print(f'{bcolors.FAIL}Error: unknown player type for player 1{bcolors.ENDC}')
        return
    
    # Check if syntax for player type 2 is valid
    try:
        p2_idx = argv.index('-p2') + 1
        p2 = argv[p2_idx]
    except ValueError:
        print(f'{bcolors.FAIL}Error: please use the correct syntax: python game_of_21.py -p1 <player_type> -p2 <player_type> [Optional: --rand <int>]{bcolors.ENDC}')
        return
        
    # Get player type for player 2
    p2_type = get_player_type(p2)
    if p2_type == -1:
        print(f'{bcolors.FAIL}Error: unknown player type for player 2{bcolors.ENDC}')
        return
    
    # Get the optional input rand
    try:
        rand_idx = argv.index('--rand') + 1
        rand = int(argv[rand_idx])
    except ValueError:
        rand = 0
        
    if (rand < 0) or (rand > 2):
        print(f'{bcolors.FAIL}Error: random type is out of bounds{bcolors.ENDC}')
        return
        
    game = GameOf21()
    game.initilize((p1_type, p2_type), RandType(rand))
    game.run()
    

if __name__ == '__main__':    
    main(sys.argv)
