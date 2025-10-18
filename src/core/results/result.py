from typing import Generic, Optional, TypeVar

from .error import Error

TValue = TypeVar('TValue')


class Result:
    def __init__(self, is_success: bool, error: Error):
        if (is_success and error != Error.NONE) or (not is_success and error == Error.NONE):
            raise ValueError("Invalid error")
        self._is_success = is_success
        self._error = error

    @property
    def is_success(self) -> bool:
        return self._is_success

    @property
    def is_failure(self) -> bool:
        return not self._is_success

    @property
    def error(self) -> Error:
        return self._error

    @staticmethod
    def success() -> 'Result':
        return Result(True, Error.NONE)

    @staticmethod
    def success_value(value: TValue) -> 'ResultValue[TValue]':
        return ResultValue(value, True, Error.NONE)

    @staticmethod
    def failure(error: Error) -> 'Result':
        return Result(False, error)

    @staticmethod
    def failure_value(error: Error) -> 'ResultValue[TValue]':
        return ResultValue(None, False, error)


class ResultValue(Result, Generic[TValue]):
    def __init__(self, value: Optional[TValue], is_success: bool, error: Error):
        super().__init__(is_success, error)
        self._value = value

    @property
    def value(self) -> TValue:
        if not self.is_success:
            raise ValueError("The value of a failure result can't be accessed.")
        return self._value

    @staticmethod
    def validation_failure(error: Error) -> 'ResultValue[TValue]':
        return ResultValue(None, False, error)
