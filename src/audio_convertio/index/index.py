import argparse
import sys
import os
from audio_convertio.classes.audio_converter import Audio
from audio_convertio.classes.custom_exceptions import WrongNumberOfArguments, InvalidArguments, IsAFile, DirectoryNotExists
from audio_convertio.shared_library.arguments_validator import dir_accessible


def convert(args: argparse.Namespace):
    try:
        dir_accessible(args.audio_dir)
        audio = Audio(args.audio_dir, args.input_format)
        audio.convert_files(args.output_format)

    except IsAFile:
        print('[ERROR] DIRECTORY_PATH SHOULD BE A DIRECTORY.')
        sys.exit(2)
    except DirectoryNotExists:
        print('[ERROR] DIRECTORY DOES NOT EXIST. YOU SHOULD USE AN EXISTING DIRECTORY.')
        sys.exit(2)
    except:
        sys.exit(2)
