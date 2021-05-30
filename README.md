# File Converter

![demonstration](https://cdn.discordapp.com/attachments/539836343094870016/835936570191511622/unknown.png)

## Table of Contents

<!--ts-->

- [About](#about)
- [Requirements](#requirements)
- [How to use](#how-to-use)
  - [Setting up Program](#program-setup)
- [Technologies](#technologies)
<!--te-->

## About

An audio converter that allows you to convert your audio files with a single command to any audio format that you want.

## Requirements

To run this repository by yourself you will need to install python3 in your machine.

## How to use

### Program Setup

```bash
# Clone this repository
$ git clone <https://github.com/AudioConvertio/file-converter>

# Access the project page on your terminal
$ cd file-converter

# Install all the requirements
$ pip install .

# Execute the program with parameters
$ audio_convertio  <path_to_audios_directory> <input_format> <output_format>

# Them it's just wait for the code run and the converted audio file will be in the same folder of the audio file passed as argument
```

![demonstration](https://cdn.discordapp.com/attachments/539836343094870016/838615313435459584/unknown.png)

## Technologies

- Python3
- Pytest
- Pydub
- Multiprocessing
