class Rules(object):
    def __init__(self) -> None:
        self.__misere = False
        self.__singleplayer = True
        self.__coins = 21
        self.__min_take = 1
        self.__max_take = 3
        
    @property
    def misere(self):
        return self.__misere
    
    @misere.setter
    def misere(self, misere: bool):
        self.__misere = misere
        
    @property
    def singleplayer(self):
        return self.__singleplayer
    
    @misere.setter
    def singleplayer(self, singleplayer: bool):
        self.__singleplayer = singleplayer
        
    @property
    def coins(self):
        return self.__coins

    @coins.setter
    def coins(self, coins: int):
        min_value = self.__min_take + self.__max_take
        max_value = 500
        if coins not in range(min_value, max_value):
            raise ValueError(f'Please select a value between {min_value} and {max_value}.')
        self.__coins = coins
        