class Rules(object):
    def __init__(self) -> None:
        self.__VALUE_IN_RANGE_HINT = 'Please enter a value between {} and {}.'
        self.__misere = False
        self.__coins = 21
        self.__min_take = 1
        self.__max_take = 3
        
    @property
    def misere(self) -> bool:
        return self.__misere
    
    @misere.setter
    def misere(self, misere: bool) -> None:
        self.__misere = misere
        
    @property
    def coins(self) -> int:
        return self.__coins

    @coins.setter
    def coins(self, amount: int) -> None:
        min_value = self.min_take + self.max_take
        max_value = 500
        if amount not in range(min_value, max_value):
            raise ValueError(self.__VALUE_IN_RANGE_HINT.format(min_value, max_value))
        self.__coins = amount
        
    @property
    def min_take(self) -> int:
        return self.__min_take
    
    @min_take.setter
    def min_take(self, amount: int) -> None:
        min_value = 1
        max_value = self.max_take
        if amount not in range(min_value, max_value):
            raise ValueError(self.__VALUE_IN_RANGE_HINT.format(min_value, max_value))
        self.__min_take = amount
    
    @property
    def max_take(self) -> int:
        return self.__max_take
    
    @max_take.setter
    def max_take(self, amount: int) -> None:
        min_value = self.min_take
        max_value = 10
        if amount not in range(min_value, max_value):
            raise ValueError(self.__VALUE_IN_RANGE_HINT.format(min_value, max_value))
        self.__max_take = amount
        