#!/usr/bin/env python3
import os

from multiprocessing import Pool, cpu_count
from pydub import AudioSegment


class Audio():
    """ Represents the audio with the path and type

    Args:
        audios_dir (str): the path where the audio is stored
        input_format (str): the format of the files to be converted
        output_format (str): the file output format
    """

    def __init__(self, audios_dir: str, input_format: str, output_format: str):
        self.audios_dir = audios_dir
        self.input_format = input_format
        self.output_format = output_format

    def __repr__(self) -> str:
        return f"This is my audio_path: {self.audios_dir} and this is my audio input: {self.input_format}"

    def convert_files_sequential(self) -> None:
        """Iterates over every file in the dir with the input_format and
        converts it to the output_format in a sequential way
        """
        for file in os.listdir(self.audios_dir):
            if file.endswith(self.input_format):
                self.convert_file(os.path.join(
                    self.audios_dir, file), self.output_format)

    def convert_files_parallel(self) -> None:
        """Iterates over every file in the dir with the input_format and
        converts it to the output_format in a parallel way
        """
        file_paths = []
        for file in os.listdir(self.audios_dir):
            if file.endswith(self.input_format):
                file_paths.append(os.path.join(
                    self.audios_dir, file))
        with Pool(cpu_count()) as p:
            p.map(self.convert_file, file_paths)

    def convert_file(self, file_path: str) -> None:
        """Converts the current audio to a new output format

        Args:
            file_path (str): path of the file to be converted
        """
        print(
            f"Converting {os.path.split(file_path)[1]} to {self.output_format}")

        output = AudioSegment.from_file(file_path, format=self.output_format)
        output.export(file_path.replace(self.input_format,
                      f'{self.output_format}'), format=self.output_format)
