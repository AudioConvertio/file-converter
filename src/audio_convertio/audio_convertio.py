import sys
import argparse
from audio_convertio.classes.audio_converter import Audio
from audio_convertio.classes.custom_exceptions import WrongNumberOfArguments, InvalidArguments, IsAFile, DirectoryNotExists
from audio_convertio.shared_library.arguments_validator import dir_accessible

NUMBER_OF_ARGUMENTS = 4


def main(argv: list) -> None:
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "audio_dir", help="The Directory where the audios are stored")
        parser.add_argument(
            "input_format", help="The format of the audios to be converted")
        parser.add_argument(
            "output_format", help="The format that the audios will be converted")

        args = parser.parse_args()
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
        raise
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
