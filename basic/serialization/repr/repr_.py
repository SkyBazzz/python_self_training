from dataclasses import dataclass
import logging
from collections import namedtuple


class Player:
    def __init__(self, p_id, name, keys):
        self.p_id = p_id
        self.name = name
        self.keys = keys

    def __repr__(self):
        cls = self.__class__.__name__
        return f'{cls}({self.p_id!r}, {self.name!r}, {self.keys!r})'


@dataclass
class Coach:
    c_id: int
    name: str
    keys: set


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='game.log')

    p1 = Player(1, 'Shevchenko', {'cooper', 'jade'})
    logging.info('p1 is %r', p1)
    logging.info(p1)

    Player = namedtuple('Player', 'p_id name keys')
    p2 = Player(1, 'Shevchenko', {'cooper', 'jade'})
    print(repr(p2))

    c1 = Coach(2, 'Ruben', {'cooper', 'jade'})
    print(repr(c1))
