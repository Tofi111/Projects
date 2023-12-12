from enum import Enum


class Response(Enum):
    PASS = 0
    FAIL = 1


globals().update(Response.__members__)
