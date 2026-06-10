import re
from typing import Callable

def generator_numbers(text: str):
    numbers = re.findall(r"\s\d+\.\d+\s", text)
    for i in numbers:
        yield i

def sum_profit(text: str, func: Callable[[str], int]):
    numbet_list = func(text)
    total = 0
    for i in numbet_list:
        total += float(i)
    return total