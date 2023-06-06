import datetime

import eyed3
import glob
import re
import os

path = "D:\\음악\\38\\*.mp3"
file_list = glob.glob(path)


def change_name(name):
    newname = ' - '.join(name.split(' - ')[:2])
    newname = newname.split('(')[0].split('[')[0]
    if newname[-4:] == '.mp3':
        return newname
    else:
        return newname + '.mp3'

def change_title(title):
    reg_pre = re.compile(r"([^-]+)\s-\s")
    reg_suf = re.compile(r"(\s\(|\s\[)(.+)")
    title = reg_pre.sub("", title, count=1)
    title = reg_suf.sub("", title, count=1)
    try:
        return title
    except AttributeError:
        print("title error")

for mp3 in file_list:
    audio = eyed3.load(mp3)
    print(f"{audio.tag.title} >>> ", end="")
    audio.tag.title = change_title(audio.tag.title)

    # try:
    #     audio.tag.title = audio.tag.title.split(' - ')[1].split('(')[0].split('[')[0]
    # except IndexError:
    #     audio.tag.title = audio.tag.title.split(' - ')[0].split('(')[0].split('[')[0]
    # audio.tag.title =  audio.tag.title.split(' - ')[-1]

    print(f"{audio.tag.title}")
    audio.tag.artist = "nightcore"
    audio.tag.save()
    try:
        os.rename(mp3, change_name(mp3))
    except FileExistsError:
        "already file exist"
