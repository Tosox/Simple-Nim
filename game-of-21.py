from rules import Rules
import random    

class GameOf21(object):
    def __init__(self, rules: Rules = Rules()) -> None:
        self.__rules = rules

    def start(self) -> None:
        coins = self.__rules.coins
        player = random.choice([False, True])

        # Main loop
        try:
            while (coins > 0):
                coins = self.__player_turn(coins, player) if ((self.__rules.singleplayer) and (not player)) else self.__computer_turn(coins, player)
                player = not player # Other players turn
        except KeyboardInterrupt:
            print('\n\n****Script cancelled by user****')
            exit()

    def __player_turn(self, coins: int, player: bool) -> int:
        self.__print_game(coins, player)

        while True:
            # Player is stuck until he gives valid input
            try:
                take = int(input('How many coins would you like to take?: '))
                if (self.__check_input_int(take, self.min_coins, self.max_coins + 1)):
                    break
                print('\n****Invalid number****')
                self.__print_game(coins, player)
            except ValueError:
                print('\n****Invalid input****')
                self.__print_game(coins, player)

        coins -= take
        if (coins <= 0):
            print('\n****Player {} wins!****'.format(((not player) + 1) if (self.__rules.misere) else (player + 1)))
        return coins

    def __computer_turn(self, coins: int, player: bool) -> int:
        self.__print_game(coins, player)

        # Calculate possible winning move
        should_take = (coins - self.__rules.misere) % (self.min_coins + self.max_coins)
        if (should_take != 0) and (self.__check_input_int(should_take, self.min_coins, self.max_coins + 1)):
            take = should_take
        else:
            take = random.randint(self.min_coins, self.max_coins)    

        print(f' -Takes {take} coin(s)')
        coins -= take
        if coins <= 0:
            print('\n****Player {} wins!****'.format(((not player) + 1) if (self.__rules.misere) else (player + 1)))
        input('Press <ENTER> to continue')
        return coins

    def __print_game(self, coins: int, player: bool) -> None:
        self.__print_line()
        print(f'Total coins: {coins} | Player: {player + 1}')

    def __print_line(self) -> None:
        print('==================================================')
        

if __name__ == '__main__':
    game = GameOf21()
    game.start()
    