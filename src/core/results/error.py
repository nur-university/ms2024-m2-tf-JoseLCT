import re

from src.core.results import ErrorType


class Error:
    NONE = None
    NULL_VALUE = None

    def __init__(
            self,
            code: str,
            structured_message: str,
            error_type: ErrorType,
            *args,
    ):
        self._code = code
        self._structured_message = structured_message or ""
        self._type = error_type
        self._description = self._build_message(self._structured_message, args)

    def _build_message(self, structured_message: str, *args) -> str:
        if not args:
            return structured_message or ""
        placeholders = re.findall(r"\{(\w+)}", structured_message)
        result = structured_message
        for i, placeholder in enumerate(placeholders):
            if i >= len(args):
                break
            value = str(args[i]) or ""
            result = result.replace(f'{{{placeholder}}}', value)
        return result

    @property
    def code(self) -> str:
        return self._code

    @property
    def description(self) -> str:
        return self._description

    @property
    def structured_message(self) -> str:
        return self._structured_message

    @property
    def type(self) -> ErrorType:
        return self._type

    @staticmethod
    def failure(code: str, structured_message: str, *args) -> 'Error':
        return Error(code, structured_message, ErrorType.FAILURE, *args)

    @staticmethod
    def not_found(code: str, structured_message: str, *args) -> 'Error':
        return Error(code, structured_message, ErrorType.NOT_FOUND, *args)

    @staticmethod
    def problem(code: str, structured_message: str, *args) -> 'Error':
        return Error(code, structured_message, ErrorType.PROBLEM, *args)

    @staticmethod
    def conflict(code: str, structured_message: str, *args) -> 'Error':
        return Error(code, structured_message, ErrorType.CONFLICT, *args)

    def __repr__(self):
        return f"Error(code='{self._code}', description='{self._description}', type={self._type})"


Error.NONE = Error("", "", ErrorType.FAILURE)
Error.NULL_VALUE = Error("General.Null", "Null value was provided", ErrorType.FAILURE)
