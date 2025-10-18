from src.core.results import Error


class DomainException(Exception):
    def __init__(self, error: Error):
        self._error = error
        super().__init__(error.description)

    @property
    def error(self) -> Error:
        return self._error
