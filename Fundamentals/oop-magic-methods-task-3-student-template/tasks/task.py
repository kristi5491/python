from __future__ import annotations
from typing import Type


class Currency:
    """
    1 EUR = 2 USD = 100 GBP

    1 EUR = 2 USD    ;  1 EUR = 100 GBP
    1 USD = 0.5 EUR  ;  1 USD = 50 GBP
    1 GBP = 0.02 USD ;  1 GBP = 0.01 EUR
    """

    exchange_rate = {
        'EUR': {'USD': 2, 'GBP': 100},
        'USD': {'EUR': 0.5, 'GBP': 50},
        'GBP': {'USD': 0.02, 'EUR': 0.01}
    }

    def __init__(self, value: float):
        self.value = value

    @classmethod
    def course(cls, other_cls: Type[Currency]) -> str:
        from_code = cls.currency_code
        to_code = other_cls.currency_code
        if from_code == to_code:
            return f'1.0 {from_code} for 1 {to_code}'
        rate = cls.exchange_rate[from_code][to_code]
        return f'{float(rate)} {to_code} for 1 {from_code}'

    def to_currency(self, other_cls: Type[Currency]):
        from_code = self.__class__.currency_code
        to_code = other_cls.currency_code
        if from_code == to_code:
            return self.__class__(self.value)
        rate = self.exchange_rate[from_code][to_code]
        converted_value = float(self.value) * float(rate)
        return other_cls(converted_value)

    def __add__(self, other: Currency) -> Currency:
        if not isinstance(other, Currency):
            return NotImplemented
        other_converted_value = float(str(other.to_currency(self.__class__)).split()[0])
        return self.__class__(self.value + other_converted_value)


    def __str__(self):
        return f'{float(self.value)} {self.__class__.currency_code}'


class Euro(Currency):
    currency_code = 'EUR'

    def __str__(self):
        return f'{float(self.value)} EUR'


class Dollar(Currency):
    currency_code = 'USD'

    def __str__(self):
        return f'{float(self.value)} USD'


class Pound(Currency):
    currency_code = 'GBP'

    def __str__(self):
        return f'{float(self.value)} GBP'


print(
    f"Euro.course(Pound)   ==> {Euro.course(Pound)}\n"
    f"Dollar.course(Pound) ==> {Dollar.course(Pound)}\n"
    f"Pound.course(Euro)   ==> {Pound.course(Euro)}\n"
)
Euro.course(Pound)
Dollar.course(Pound)
Pound.course(Euro)

e = Euro(100)
r = Pound(100)
d = Dollar(200)

print(
    f"e = {e}\n"
    f"e.to_currency(Dollar) = {e.to_currency(Dollar)}\n"
    f"e.to_currency(Pound) = {e.to_currency(Pound)}\n"
    f"e.to_currency(Euro)   = {e.to_currency(Euro)}\n"
)

e = Euro(100)
r = Pound(100)
d = Dollar(200)
print(
    f"e + r  =>  {e + r}\n"
    f"r + d  =>  {r + d}\n"
    f"d + e  =>  {d + e}\n"
)
# e + r  =>  101.0 EUR  # Euro instance printed
# r + d  =>  10100.0 GBP  # Pound instance printed
# d + e  =>  400.0 USD  # Dollar instance printed
