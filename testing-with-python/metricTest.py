import random


def fn(x, y):
    """A function which performs a sum."""
    return x + y


def find_optimal_route_to_my_office_from_home(
        start_time, expected_time, favorite_route='SBS1K',
        favorite_option='bus'):
    d = (expected_time - start_time).total_seconds() / 60.0

    if d <= 30:
        return 'car'
    elif 30 < d < 45:
        return ('car', 'metro')
    elif d > 45:
        if d < 60:
            return ('bus:335E', 'bus:connector')
        elif d > 80:
            return random.choice(
                ('bus:330', 'bus:331', 
                 ':'.join((favorite_option, favorite_route)))
            )
        elif d > 90:
            return ':'.join((favorite_option, favorite_route))


class C:
    """A class which does almost nothing."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self):
        pass

    def g(self, x, y):
        if self.x > x:
            return self.x + self.y
        else:
            return x + self.y


class D(C):
    """D class."""
    def __init__(self, x, y):  # Added 'y' as a parameter here
        super().__init__(x, y)

    def f(self, x, y):
        if x > y:
            return x - y
        else:
            return x + y

    def g(self, y):
        if self.x > y:
            return self.x + y
        else:
            return y - self.x
