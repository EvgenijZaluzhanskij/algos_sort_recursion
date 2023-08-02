"""
Число способов разменять сумму А с помощью N типов монет равно сумме:
    1) Число способов разменять сумму А с помощью всех типов монет, кроме первого типа момент
    2) Число способов разменять сумму (А - D) с использованием всех N типов,
       где D - номинал монеты первого типа

Допущения:

В разбиение может быть 0 монет какого-то типа

Условия:

Если A равно 0 - это значит, что есть только 1 способ размена
Если A меньше 0 - это значит, что есть 0 способов размена
Если N равно 0 - это значит, что есть 0 способов размена


Пример:

Есть монеты номиналом: 1, 5, 10, 25, 50
Необходимо разменять: 20
Количество типов монет: 3

Алгоритм:

1) Выбираем первую тройку типов монет: 1, 5, 10
2) Выбираем любой тип монетки из п.1: 1
3) Так как не знаем количество итераций - подойдет рекурсия.
   Для рекурсии необходимо уменьшение объема данных на каждом шаге.

   Можем выделить 2 этапа:
   1) Считаем количество разбиений, в которых нет монет с номиналом 1
   2) Считаем количество разбиений, в которых есть как минимум 1 монета с номиналом 1

4) Каждый этап является точной копией исходных данных из п.2 - выделяем рекурсивную функцию:

   func(amount, coin_types)

   amount - сумма, которую разбиваем
   coin_types - типа монет, которыми разбиваем

   Получается два рекурсивных вызова:

   func(20, [5, 10]) + func(19, [1, 5, 10])

5) Повторяем до тех пор, пока каждая рекурсия не достигнет базы.
"""
import itertools

from typing import List


all_kinds_of_coins = [1, 5, 10, 25, 50]


def prepare_combinations(combination_size: int):
    return itertools.combinations(all_kinds_of_coins, combination_size)


def count_exchanges(amount: int, kind_of_coins: List[int]) -> int:
    # Если уменьшением суммы достигли 0 - корректный размен
    if amount == 0:
        return 1

    # Если уменьшением получили меньше 0 или закончились типа монеток - разбиение завершаем
    if amount < 0 or len(kind_of_coins) == 0:
        return 0

    excluded_coin = kind_of_coins[0]

    without_one_coin_type = count_exchanges(amount, kind_of_coins[1:])

    without_one_coin_type_nominal = count_exchanges(amount - excluded_coin, kind_of_coins)

    return without_one_coin_type + without_one_coin_type_nominal


def solution(amount: int, count_of_kinds: int) -> int:
    result = 0
    for kind_of_coins in prepare_combinations(count_of_kinds):
        result += count_exchanges(amount, list(kind_of_coins))

    return result


if __name__ == '__main__':
    print(solution(0, 2))
