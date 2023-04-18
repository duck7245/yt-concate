# 1. get all video list from a channel

import urllib.request
import json
from yt_concate.settings import API_KEY

# CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA' # global 的用全大寫來示意内容不變
# print(API_KEY)
CHANNEL_ID = API_KEY


def get_all_video_in_channel(channel_id):
    api_key = 'AIzaSyD9TmtcASTSq0Q3yEO5DcEg0A70JYP7JRw'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'  # 跟 api 拿網址

    first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key,
                                                                                                        channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)  # 丟出去的網址
        resp = json.load(inp)  # 回傳的網址

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except KeyError:
            break
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))

# 2. download youtube subtitle
# 3. download youtube video
# 4. edit video
