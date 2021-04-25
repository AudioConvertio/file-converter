import sys
import getopt
from classes.custom_exceptions import WrongNumberOfArguments, InvalidArguments, FileNotExists, FileInaccessible
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

        print(f'Input file is {input_file}')
        print(f'Output file is {output_format}')

        file_accessible(input_file)

    except WrongNumberOfArguments:
        print("[ERROR] INVALID NUMBER OF ARGUMENTS")
        print('main.py -i <inputfile> -o <outputformat>')
        sys.exit(2)
    except InvalidArguments:
        print('[ERROR] WRONG ARGUMENTS')
        print('main.py -i <inputfile> -o <outputformat>')
        sys.exit(2)
    except FileNotExists:
        print('[ERROR] FILE DOES NOT EXIST')
        print('main.py -i <inputfile> -o <outputformat>')
        sys.exit(2)
    except FileInaccessible:
        print('[ERROR] FILE IS INACESSIBLE')
        print('main.py -i <inputfile> -o <outputformat>')
        sys.exit(2)
    except:
        print('[ERROR] AN UNEXPECTED ERROR OCCURRED.')
        sys.exit(2)


if __name__ == "__main__":
    main(sys.argv[1:])
