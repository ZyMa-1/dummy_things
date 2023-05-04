import itertools
import math
from collections.abc import Iterable as IterableObject
from decimal import Decimal
from typing import Iterable as IterableType


def multiply(*args: Decimal | IterableType) -> Decimal:
    numbers = itertools.chain(args)
    ans = Decimal(1.0)
    for obj in numbers:
        if ans == 0.0:
            return ans
        if isinstance(obj, IterableObject):
            for element in obj:
                ans *= Decimal(element)
        elif isinstance(obj, Decimal):
            ans *= obj
        else:
            raise ValueError
    return ans


def cumulative_probability(*, prob: float, res: int, total: int) -> Decimal:
    prob = Decimal(prob)
    i_prob = 1 - prob
    ans = Decimal(0.0)
    for cur_res in range(res, total + 1):
        ans += multiply([i_prob for _ in range(total - cur_res)], [prob for _ in range(cur_res)],
                        Decimal(math.comb(total, cur_res)))
    return ans
