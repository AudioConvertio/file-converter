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

To run this repository by yourself you will need to install python3 in your machine and them install all the requirements inside the [requirements](requirements.txt) file

## How to use

### Program Setup

```bash
# Clone this repository
$ git clone <https://github.com/AudioConvertio/file-converter>

# Access the project page on your terminal
$ cd file-converter

# Install all the requirements
$ pip install -r requirements.txt

# Access the src on your terminal
$ cd src

# Execute the main program with parameters
$ python main.py -i <path_to_audio_file> -o <output_format>

# Them it's just wait for the code run and the converted audio file will be in the same folder of the audio file
```

![demonstration](https://cdn.discordapp.com/attachments/539836343094870016/835936244784431134/unknown.png)

## Technologies

- Python3
- Pytest
- Pydub
