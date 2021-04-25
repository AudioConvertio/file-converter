import pytest
from shared_library.arguments_validator import load_arguments, LIST_OF_ACCEPTED_FORMATS
from classes.custom_exceptions import *


class TestArgumentsValidator(object):

    def test_load_arguments_valid_return_type(self):
        args = load_arguments([('-i', 'archive'), ('-o', 'wmv')])
        assert type(args) is list

    def test_load_arguments_valid_number_of_arguments(self):
        args = load_arguments([('-i', 'archive'), ('-o', 'wmv')])
        assert len(args), 2

    def test_load_arguments_valid_input(self):
        args = load_arguments([('-i', 'archive'), ('-o', 'wmv')])
        assert args[0] is 'archive'
        assert args[1] is 'wmv'

    def test_load_arguments_valid_format_type(self):
        args = load_arguments([('-i', 'archive'), ('-o', 'wmv')])
        assert args[1] in LIST_OF_ACCEPTED_FORMATS