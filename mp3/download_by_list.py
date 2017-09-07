from __future__ import unicode_literals
import csv
import youtube_dl
import os

filenames = []

os.environ["PATH"] += os.pathsep + "/usr/local/bin"
song_list_csv = os.path.join("..","meta_data", "fileurls.csv")
out_path = "mp3"

class logger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def tmp_filename(d):
    if d['status'] == 'finished':
        name = d['filename']
        r = name.split('-')[-1].split('.')[0] + '.mp3'
        namesplit = name.split('-')
        namesplit[-1] = r

        newname = "-".join(namesplit)

        filenames.append(newname)

        print(len(filenames), newname, 'is downloaded, now converting ...')

ydl_opts = {
    'format': 'bestaudio/best',
    'noplaylist': 'True',
    'verbose': 'True',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'logger': logger(),
    'progress_hooks': [tmp_filename],
}

def ydownload(filelist, songname):
    filenames.clear()
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(filelist)

    print("Renaming all files...")
    for idx, file in enumerate(filenames):
        os.rename(filenames[idx], "%03d-%s%s" % (idx + 1, songname[idx], '.mp3'))


def get_song_list(filename):
    table = []
    with open(filename, 'r', encoding='utf-8') as f:
        csv_cursor = csv.reader(f)
        for row in csv_cursor:
            table.append(row)

    return table[1:]  # skip header


def transpose_table(table):
    return list(map(list, zip(*table)))


table = get_song_list(song_list_csv)
tt = transpose_table(table)

filelist = tt[3][:10]
songname = tt[1][:10]

ydownload(filelist, songname)
