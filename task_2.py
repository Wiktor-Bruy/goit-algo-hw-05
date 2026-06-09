import re
from typing import Callable

def generator_numbers(text: str):
    text_list = text.strip().split()
    number_list = list(filter(lambda text: re.fullmatch(r"\d+\.\d+", text), text_list))
    number_list = [float(n) for n in number_list]
    return number_list

def sum_profit(text: str, func: Callable[[str], list[float]]):
    numbet_list = func(text)
    total = 0
    for i in numbet_list:
        total += i
    return total