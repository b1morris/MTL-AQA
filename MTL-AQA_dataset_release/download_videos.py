import os
import pandas as pd
from pytube import YouTube

#be sure to install pytube
#pip3 install --upgrade git+https://github.com/nficano/pytube
#be sure to install openpyxl
#python3 -m pip install openpyxl

#SAVE_PATH = '../../data/dataset_generation/videos'
SAVE_PATH = '/home/morrisb4/shared/data/AQA/Videos'
os.makedirs(SAVE_PATH, exist_ok=True)

#df = pd.read_excel('Video_List.xlsx', engine='openpyxl', sheet_name='Sheet1')
df = pd.read_csv('Video_List.csv')    #convert xlsx to csv file if openpyxl not working

list_urls = df['url']
#list_urls = ['https://www.youtube.com/watch?v=cYkUl8MrXgA']

print("Total number of videos :", len(list_urls))
count = 0
for url in list_urls:
    count += 1
    vidnum = df.loc[count-1][0]
    vidname= '%02d.mp4' % vidnum
    print(count, "Video: ", vidname, " URL :", url)

    try:
        yt_obj = YouTube(url)
        title = yt_obj.title
        print("    Trying: ", title)

        yt_obj.streams.get_highest_resolution().download(output_path=SAVE_PATH, filename=vidname)
    except Exception as e:
        print(e)
        continue
        # raise Exception('Some exception occurred.')
print('All YouTube videos downloaded successfully.')
