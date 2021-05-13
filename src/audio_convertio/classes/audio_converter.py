#!/usr/bin/env python3
import os

from pydub import AudioSegment


class Audio():
    """ Represents the audio with the path and type

    Args:
        audios_dir (str): the path where the audio is stored
        input_format (str): the format of the files to be converted
    """

    def __init__(self, audios_dir: str, input_format: str):
        self.audios_dir = audios_dir
        self.input_format = input_format

    def __repr__(self) -> str:
        return f"This is my audio_path: {self.audios_dir} and this is my audio input: {self.input_format}"

    def convert_files(self, output_format: str) -> None:
        """Iterates over every file in the dir with the input_format and
        converts it to the output_format

        Args:
            output_format (str): the file output format
        """
        for file in os.listdir(self.audios_dir):
            if file.endswith(self.input_format):
                print(f"Converting {file} to {output_format}")
                self.convert_file(os.path.join(
                    self.audios_dir, file), output_format)

    def convert_file(self, file_path: str, output_format: str) -> None:
        """Converts the current audio to a new output format

        Args:
            output_format (str): the file output format
        """

        output = AudioSegment.from_file(file_path, format=output_format)
        return output.export(file_path.replace(self.input_format, f'{output_format}'), format=output_format)
