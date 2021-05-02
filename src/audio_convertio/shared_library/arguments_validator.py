#!/usr/bin/env python3
from os import path
from audio_convertio.classes.custom_exceptions import IsAFile, DirectoryNotExists

LIST_OF_ACCEPTED_FORMATS = ['wmv']


def dir_accessible(file_dir: str) -> None:
    """Tries to open the file to validate if it is accessible

    Args:
        file_dir (str): the file directory

    """
    if path.isfile(file_dir):
        raise IsAFile

    if not path.isdir(file_dir):
        raise DirectoryNotExists
