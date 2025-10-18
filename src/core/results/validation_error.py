from src.core.results import Error, ErrorType, Result


class ValidationError(Error):
    def __init__(self, errors: list[Error]):
        super().__init__(
            "Validation.General",
            "One or more validation errors occurred",
            ErrorType.VALIDATION,
        )
        self.errors = errors

    @staticmethod
    def from_results(results: list[Result]) -> "ValidationError":
        failed_errors = [r.error for r in results if r.is_failure]
        return ValidationError(failed_errors)
