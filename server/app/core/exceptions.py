

class AppException(Exception):
    pass

class NotFounfException(AppException):
    pass


class ConflictException(AppException):
    pass

class ValidationException(AppException):
    pass