from functools import reduce


class Calc:
    def add(self, *args):
        return sum(args)

    def sub(self, a, b):
        return a - b

    def mul(self, *args):
        if not all(args):
            raise ValueError
        return reduce(lambda x, y: x*y, args)

    def div(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            return "inf"

    def avg(self, it, lt=None, ut=None):
        if not len(it):
            return 0

        if not lt:
            lt = min(it)

        if not ut:
            ut = max(it)

        _it = [x for x in it if x >= lt and x <= ut]

        return sum(_it)/len(_it)
