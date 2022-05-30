from decimal import Decimal
from collections import namedtuple
from typing import Callable, Optional, Tuple
import functools, random


class RandomDecimalNumber:
    __range__ = namedtuple(
            typename="range",
            field_names=["start", "stop"]
        )

    def __init__(
            self, 
            domain: Tuple[int, int],
            figure: int = 3, 
            count: Optional[int] = None
        ) -> None:
        """
        Prepare require attributes for a collection of random decimal numbers.

        Args:
            domain (Required) : A tuple that the class considers its two first indexes. 
            The arguments are called 'start' and 'stop'. If they're equaled, the result always is 'start'. 
            If 'stop' is greater than 'stop', their values will be transfered.
            Remember that 'stop' always is reduced one.

            figure (Optional) : Count of decimal figures. (default=3)

            count (Optional) : Count of random numbers.
            If you have no limit to use them, pass it to None. (default=None)
        """
        
        self.integer: Optional[int] = None
        self.decimal: Optional[int] = None
        self.absoloute_value: Optional[int] = None
        self.values: list[Decimal] = []
        self.count = count
        self.figure = figure
        self._random_stop_flag = int("9" * figure)
        self._start = domain[0]
        self._stop = domain[1] - 1
        
        if self._start > self._stop:
            self.range = self.__range__(self.stop, self.start)
            self._start, self._stop = self.stop, self.start

        elif self._start == self._stop:
            self.absoloute_value = self._start
        
        self.range = self.__range__(self.start, self.stop)

    @property
    def start(self):
        """Returns start point."""
        return self._start

    @property
    def stop(self):
        """Returns end point."""
        return self._stop

    def check_count(func: Callable):
        """
        A decorator based on checking 'count' and count of 'values' attributes.
        If they're equal, the next decimal number won't be generated.
        """
        @functools.wraps(func)
        def wrapper(self):
            if self.count != len(self.values):
                return func(self)
            raise StopIteration
        return wrapper

    def generate_number(self) -> Decimal:
        """Generate the next random number."""
        self.integer = random.randint(self.start, self.stop)
        self.decimal = random.randint(0, self._random_stop_flag) / (10 ** self.figure)
        result = Decimal(self.integer + self.decimal)
        self.values.append(result)
        return result

    def __str__(self) -> str:
        """Returns RandomDecimalNumber(start, stop)."""
        return f"{self.__class__.__name__}({self.range.start, self.range.stop})"
    
    def __iter__(self):
        return self

    @check_count
    def __next__(self) -> Decimal:
        """Generate the next decimal number."""
        if self.absoloute_value:
            self.count = 1
            self.values.append(self.absoloute_value)
            return self.absoloute_value
        return round(self.generate_number(), self.figure)
    
    def __call__(self) -> Callable:
        return self.__next__()
