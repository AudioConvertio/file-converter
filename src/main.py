import sys
import getopt
from classes.audio_converter import Audio
from classes.custom_exceptions import WrongNumberOfArguments, InvalidArguments, FileNotExists, FileInaccessible, IsADirectory
from shared_library.arguments_validator import load_arguments, file_accessible

NUMBER_OF_ARGUMENTS = 4


def main(argv: list) -> None:
    try:
        if len(argv) != NUMBER_OF_ARGUMENTS:
            raise WrongNumberOfArguments
        try:
            opts, args = getopt.getopt(argv, "i:o:", ["ifile=", "oformat"])
        except getopt.GetoptError:
            raise InvalidArguments

        input_file, output_format = load_arguments(opts)

        file_accessible(input_file)

        audio = Audio(input_file)
        print(audio)
        audio.convert_file(output_format)

    except WrongNumberOfArguments:
        print("[ERROR] INVALID NUMBER OF ARGUMENTS.")
        print('main.py -i <inputfile> -o <outputformat>')
        sys.exit(2)
    except InvalidArguments:
        print('[ERROR] WRONG ARGUMENTS.')
        print('main.py -i <inputfile> -o <outputformat>')
        sys.exit(2)
    except FileNotExists:
        print('[ERROR] FILE DOES NOT EXIST. YOU SHOULD USE AN EXISTING FILE.')
        sys.exit(2)
    except FileInaccessible:
        print('[ERROR] FILE IS INACESSIBLE. PLEASE, CHECK THE PERMISSIONS ')
        sys.exit(2)
    except IsADirectory:
        print('[ERROR] FILE_PATH SHOULD BE AN AUDIO.')
        sys.exit(2)
    except:
        print('[ERROR] AN UNEXPECTED ERROR OCCURRED.')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
