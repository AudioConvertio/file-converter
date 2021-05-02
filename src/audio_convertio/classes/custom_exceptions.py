#!/usr/bin/env python3
class Error(Exception):
    """Base class for other exceptions
    """
    pass


class WrongNumberOfArguments(Error):
    """Raised when the number of arguments is different from the expected
    """
    pass


class InvalidArguments(Error):
    """Raised when the arguments are different from the expected
    """
    pass


class DirectoryNotExists(Error):
    """Raised when the file doesn't exists
    """
    pass


class IsAFile(Error):
    """Raised when the file_path is not a directory
    """
    pass
