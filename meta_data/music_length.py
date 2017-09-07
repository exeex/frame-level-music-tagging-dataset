from __future__ import unicode_literals
from mutagen.mp3 import MP3
import os
import math
import csv

table = []
mp3_path = os.path.join("..", "mp3")

for root, dirs, files in os.walk(mp3_path):
    files.sort()
    for file in files:
        try:
            pathandname = os.path.join(root, file)
            audio = MP3(pathandname)
            print(pathandname)
            length = audio.info.length
            table.append([math.floor(length),file])
        except:
            print(file)

with open('timelist.csv', 'wt',newline='', encoding='utf-8') as f:
    csvout = csv.writer(f)
    for idx, row in enumerate(table):
        csvout.writerow([idx+1]+row)
