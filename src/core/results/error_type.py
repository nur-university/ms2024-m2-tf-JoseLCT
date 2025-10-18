from enum import Enum


class ErrorType(Enum):
    FAILURE = 0
    VALIDATION = 1
    PROBLEM = 2
    NOT_FOUND = 3
    CONFLICT = 4
