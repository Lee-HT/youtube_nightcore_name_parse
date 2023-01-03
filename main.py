import eyed3
import glob
import os

path = "D:\\음악\\37\\*.mp3"
file_list = glob.glob(path)

def changename(name):
    newname = ' - '.join(name.split(' - ')[:2])
    newname = newname.split('(')[0].split('[')[0]
    if newname[-4:] == '.mp3':
        print('if')
        return newname
    else:
        print('else')
        return newname + '.mp3'

for mp3 in file_list:
    audio = eyed3.load(mp3)
    try:
        audio.tag.title =  audio.tag.title.split(' - ')[1].split('(')[0].split('[')[0]
    except IndexError:
        audio.tag.title = audio.tag.title.split(' - ')[0].split('(')[0].split('[')[0]
    # audio.tag.title =  audio.tag.title.split(' - ')[-1]
    print(audio.tag.title)
    audio.tag.artist = "nightcore"
    audio.tag.save()
    os.rename(mp3,changename(mp3))