import eyed3
import glob
import re
import os

extension = "mp3"
path = f"D:\\음악\\39\\*.{extension}"
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

print("files :",file_list)
for music in file_list:
    if extension == "mp3":
        audio = eyed3.load(music)
        print(f"{audio.tag.title} >>> ", end="")
        audio.tag.title = change_title(audio.tag.title)
        print(f"{audio.tag.title}")
        audio.tag.artist = "nightcore"
        audio.tag.save()
    else:
        pass

    try:
        os.rename(music, change_name(music))
    except FileExistsError:
        "already file exist"
