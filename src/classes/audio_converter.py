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
        self.audio_type = ""

    def _set_audio_type(self) -> None:
        """Gets the extension and sets it to audio_type
        """
        name, extension = os.path.splitext(self.audio_path)
        self.audio_type = extension
