import pandas as pd
import pickle
import os
from pydub import AudioSegment

required_juz = input('Enter Required juz number: \n')
a = pd.read_csv("manual-excel-entries-{}.csv".format(required_juz), delimiter="\t", header=None)
lst = [] 
for i in [str(i) for i in list(a[0])]:
    s = i.split(".")
    seconds = (int(s[1]) + (int(s[0]) * 60))*1000
    lst.append(seconds)
a['from_seconds'] = lst

lst = [] 
for i in [str(i) for i in list(a[1])]:
    s = i.split(".")
    seconds = (int(s[1]) + (int(s[0]) * 60))*1000
    lst.append(seconds)
a['to_minutes'] = lst


df = a[['from_seconds', 'to_minutes']]
audio_file = "2-baqra"
sound = AudioSegment.from_mp3(audio_file)

for e,i in enumerate(zip(list(df['from_seconds']), list(df['to_minutes']))):
    audiofile = sound[i[0]:i[1]+1]
    audiofile.export(str(e+1)+".mp3", format="mp3")
