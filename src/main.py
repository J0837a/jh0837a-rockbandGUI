import requests as API
import webbrowser as web
import pygame as pyg
#import math as meh

yt_vid = "https://www.youtube.com/watch?v=Oo8H5vUKMlk"

params = {
    "url": yt_vid,
    "format": 'mp3',
}

headers = {
        'X-RapidAPI-Key': '09ff266df6msh583568c18c6ed0bp116179jsn2292c3aa22f6',
        'X-RapidAPI-Host': 't-one-youtube-converter.p.rapidapi.com'
}

raw_video_obj = API.get("https://t-one-youtube-converter.p.rapidapi.com/api/v1/createProcess", headers=headers,  params=params)
converted_video_obj = raw_video_obj.json()
web.open(converted_video_obj["file"])

#for x in range(1, 100):
#   if meh.ceil(x / 2) == x / 2:
#        print(x)
