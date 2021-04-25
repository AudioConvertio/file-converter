import os

import matplotlib.pyplot as plt
import numpy as np

from pydub import AudioSegment
from pydub.playback import play


class Audio():
    """ Represents the audio with the path and type

    Args:
        audio_path (str): the path where the audio is stored
    """

    def __init__(self, audio_path: str):
        self.audio_path = audio_path
        self.audio_type = self._set_audio_type()

    def _set_audio_type(self) -> None:
        """Gets the extension and sets it to audio_type
        """
        name, extension = os.path.splitext(self.audio_path)
        return extension

    def __repr__(self) -> str:
        return f"This is my audio_path: {self.audio_path} and this is my_audio_type: {self.audio_type}"

    def convert_file(self, output_format: str) -> None:
        """Converts the current audio to a new output format

        Args:
            output_format (str): the file output format
        """
        output = AudioSegment.from_file(self.audio_path, format=output_format)
        return output.export(self.audio_path.replace(self.audio_type, f'.{output_format}'), format="mp3")
