import urllib.request, json
from selenium import webdriver
import time

def lookForNewVideo():

    apiKey = "AIzaSyDr-TtzWlvN_fnZwrlJf7bGNtbVn0-UPtI"
    channelId = "UCiWphW3UbbuG7FR3sAr3b0A"

    baseVideoUrl = "https://www.youtube.com/watch?v="
    baseSearchUrl = "https://www.googleapis.com/youtube/v3/search?"

    url = baseSearchUrl + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=1'.format(apiKey, channelId)

    inp = urllib.request.urlopen(url)
    resp = json.load(inp)

    vidId = resp['items'][0]['id']['videoId']
    
    videoExists = False
    with open('videoid.json', 'r') as json_file:
        data = json.load(json_file)

    if data['videoId'] != vidId :

        driver = webdriver.Firefox()
        driver.get(baseVideoUrl + vidId)
        videoExists = True

    if videoExists:
        with open('videoid.json', 'w') as json_file:
            data = {"videoId": vidId}
            json.dump(data, json_file)

try:
    while True:
        lookForNewVideo()
        time.sleep(10)

except KeyboardInterrupt:
    print("Sleeping")