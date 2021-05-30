#!/usr/bin/env python3
import argparse
import sys
from audio_convertio.classes.audio_converter import Audio
from audio_convertio.classes.custom_exceptions import IsAFile, DirectoryNotExists
from audio_convertio.shared_library.arguments_validator import dir_accessible


def convert(args: argparse.Namespace):
    try:
        dir_accessible(args.audio_dir)
        audio = Audio(args.audio_dir, args.input_format, args.output_format)
        audio.convert_files_parallel()

    except IsAFile:
        print('[ERROR] DIRECTORY_PATH SHOULD BE A DIRECTORY.')
        sys.exit(2)
    except DirectoryNotExists:
        print('[ERROR] DIRECTORY DOES NOT EXIST. YOU SHOULD USE AN EXISTING DIRECTORY.')
        sys.exit(2)
    except:
        print('[ERROR] UNEXPECTED ERROR. PLEASE CONTACT THE DEVELOPERS OF THIS PACKAGE.')
        sys.exit(2)
