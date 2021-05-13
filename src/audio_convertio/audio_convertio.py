#!/usr/bin/env python3
import argparse
from audio_convertio.index.index import convert


def main() -> None:
    params = {"description": __doc__}
    convert_parser = argparse.ArgumentParser(**params)
    convert_parser.add_argument(
        "audio_dir", help="The Directory where the audios are stored")
    convert_parser.add_argument(
        "input_format", help="The format of the audios to be converted")
    convert_parser.add_argument(
        "output_format", help="The format that the audios will be converted")

    convert_parser.set_defaults(func=convert)
    args = convert_parser.parse_args()
    if args.func is not None:
        args.func(args)
    else:
        convert_parser.print_help()

    return


if __name__ == "__main__":
    exit(main())
