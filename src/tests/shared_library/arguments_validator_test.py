#!/usr/bin/env python3
import pytest
from audio_convertio.shared_library.arguments_validator import dir_accessible
from audio_convertio.classes.custom_exceptions import *


class TestArgumentsValidator(object):
    def test_dir_accessible_file_is_directory(self):
        with pytest.raises(IsAFile):
            dir_accessible('LICENSE')

    def test_dir_accessible_file_not_found(self):
        with pytest.raises(DirectoryNotExists):
            dir_accessible('bat')
