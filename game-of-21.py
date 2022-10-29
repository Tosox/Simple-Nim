from pickle import TRUE
import random

class Game():
    def __init__(self) -> None:
        # Set default game settings
        self.is_game_mode_misere = False
        self.is_singleplayer = True
        self.stones = 21
        self.min_stones = 1
        self.max_stones = 3

    #
    # Public main methods
    #

    def init(self, is_game_mode_misere: bool = True, is_singleplayer: bool = True, stones: int = 21, min_stones: int = 1, max_stones: int = 3) -> None:
        # Update settings by optional user input 
        if ((self.__check_input_bool(is_game_mode_misere)) and (self.__check_input_bool(is_singleplayer)) 
            and (self.__check_input_int(stones, min_stones + max_stones, 500)) and (self.__check_input_int(min_stones, 1, max_stones + 1))):
            self.is_game_mode_misere = is_game_mode_misere
            self.is_singleplayer = is_singleplayer
            self.stones = stones
            self.min_stones = min_stones
            self.max_stones = max_stones

    def start(self) -> None:
        self.__print_rules()
        stones = self.stones
        player = random.choice([False, True])

        # Main loop
        try:
            while (stones > 0):
                stones = self.__player_turn(stones, player) if ((self.is_singleplayer) and (not player)) else self.__computer_turn(stones, player)
                player = not player # Other players turn
        except KeyboardInterrupt:
            print('\n\n****Script cancelled by user****')
            exit()
        except Exception:
            print('\n****An error occured while trying to run the game****')
            exit()

    #
    # Private main methods
    #

    def __player_turn(self, stones: int, player: bool) -> int:
        self.__print_game(stones, player)

        while True:
            # Player is stuck until he gives valid input
            try:
                take = int(input('How many stones would you like to take?: '))
                if (self.__check_input_int(take, self.min_stones, self.max_stones + 1)):
                    break
                print('\n****Invalid number****')
                self.__print_game(stones, player)
            except ValueError:
                print('\n****Invalid input****')
                self.__print_game(stones, player)

        stones -= take
        if (stones <= 0):
            print('\n****Player {} wins!****'.format(((not player) + 1) if (self.is_game_mode_misere) else (player + 1)))
        return stones

    def __computer_turn(self, stones: int, player: bool) -> int:
        self.__print_game(stones, player)

        # Calculate possible winning move
        should_take = (stones - self.is_game_mode_misere) % (self.min_stones + self.max_stones)
        if ((should_take != 0) and (self.__check_input_int(should_take, self.min_stones, self.max_stones + 1))):
            take = should_take
        else:
            take = random.randint(self.min_stones, self.max_stones)    

        print(' -Takes {} stone(s)'.format(take))
        stones -= take
        if (stones <= 0):
            print('\n****Player {} wins!****'.format(((not player) + 1) if (self.is_game_mode_misere) else (player + 1)))
        input('Press <ENTER> to continue')
        return stones
    
    #
    # Private helper methods
    #

    def __check_input_bool(self, boolean: bool) -> bool:
        try:
            if (boolean in range(0, 1 + 1)):
                return True
            return False
        except Exception:
            return False

    def __check_input_int(self, integer: int, range_start: int, range_stop: int) -> bool:
        try:
            if (integer in range(range_start, range_stop)):
                return True
            return False
        except Exception:
            return False

    def __print_rules(self) -> None:
        print('\n****Easy Game of Nim****')
        self.__print_line()
        print('How to play:')
        print(' -Goal:')
        print('  -Game mode "normal": The player who takes the last stone *wins* the game')
        print('  -Game mode "misere": The player who takes the last stone *loses* the game')
        print(' -The player who is in turn picks any number of stones')
        print(' *The requirement is that the amount is within the definied range')
        print('Notes:')
        print(' -If you enter an invalid input, the game might crash')
        print(' -Guidelines for the parameters of the "init"-method:')
        print('  -1.-Game mode: must be a boolean')
        print('  -2.-Singleplayer: must be a boolean')
        print('  -3.-Amount of stones: must be between the sum of the minimum and maximum amount of stones and 500')
        print('  -4.-Minimum amount of stones that can be taken: must be above 0')
        print('  -5.-Maximum amount of stones that can be taken: must be higher than the minimum amount of stones')
        self.__print_line()
        input('Press <ENTER> to continue')

    def __print_game(self, stones: int, player: bool) -> None:
        self.__print_line()
        print('\nTotal stones: {} | Player: {}'.format(stones, player + 1))

    def __print_line(self) -> None:
        print('==================================================')
        

if __name__ == '__main__':
    game = Game()
    game.init(True, True, 21, 1, 3)
    game.start()
    