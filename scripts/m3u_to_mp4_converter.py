# -*- coding: utf-8 -*-
"""
Converts M3U playlist to mp4 file using FFMPEG.

Requirements:
    -> Python 3.0 or higher
    -> FFMPEG installed in system path.
    -> Working internet connection for online M3U FIle.

Usage:
    -> Simply run this script with python and follow on screen instructions.
"""
__script_name__ = "M3U Playlist to Mp4 Converter Using FFMPEG"
__version__ = "0.1.0"
__author__ = "Mayank Thakur"
__date__ = "17-01-2019"

import subprocess
import os

if __name__ == "__main__":
    print("M3U Playlist to Mp4 Converter Using FFMPEG")

    link_type = input("Select type(local/URL)? ")

    if link_type.strip().lower() == "local":
        m3u_path = input("Please Give M3U File Path(Absolute): ")
        base_path, file_path = os.path.split(m3u_path)
        os.chdir(base_path)
    else:
        m3u_path = input("Please Give M3U Complete File URL(ex. https://www.abc.com/abc.m3u8): ")
        base_path = ""
        file_path = m3u_path

    print("Current working directory: {}".format(os.getcwd()))
    print("Handing over the task to FFMPEG")

    filename = os.path.splitext(file_path)[0]
    cmd = ['ffmpeg', '-allowed_extensions', 'ALL', '-i', file_path, filename+".mp4"]
    p = subprocess.run(cmd, stdout=subprocess.PIPE, universal_newlines=True)

    print(p.stdout)
    print("Output file path: {}".format(os.path.join(base_path, filename+".mp4")))
    print("Converter is Exiting now...\n\nHave a Nice Day...")
