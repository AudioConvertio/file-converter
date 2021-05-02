from audio_convertio.classes.custom_exceptions import FileNotExists, FileInaccessible, IsADirectory

LIST_OF_ACCEPTED_FORMATS = ['wmv']


def file_accessible(file_path: str) -> None:
    """Tries to open the file to validate if it is accessible

    Args:
        file_path (str): the file path

    Raises:
        FileNotExists: raises error if the file_path was not found
        FileInacessible: raises error if the file_path was inaccessible found

    """
    try:
        with open(file_path) as file:
            return

    except FileNotFoundError:
        raise FileNotExists
    except IsADirectoryError:
        raise IsADirectory
    except IOError:
        raise FileInaccessible


def load_arguments(arguments: list) -> list:
    """Parse all argv arguments

    Args:
        arguments (list): the list of arguments

    Returns:
        list: the list of arguments parsed
    """

    args = []
    for opt, arg in arguments:
        if opt in ['-h', '-help']:
            print('main.py -i <inputfile> -o <outputformat>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            args.append(arg)
        elif opt in ("-o", "--oformat"):
            args.append(arg)

    return args
