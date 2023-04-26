import urllib.request  # 理想的 import 順序: 1.内建 2.第三方 3.自已的
import json

from yt_concate.pipeline.steps.step import Step
from yt_concate.settings import API_KEY


class GetVideoList(Step):  # 繼承 class Step(ABC)
    def process(self, data, inputs):  # inputs 為 main 裡的 dictionary, data 為 pipeline 裡的 data = None
        channel_id = inputs['channel_id']  # 重要!! 意思為 input 這個 dictionary 裡的 channel_id key 的 value
        base_video_url = 'https://www.youtube.com/watch?v='
        base_search_url = 'https://www.googleapis.com/youtube/v3/search?'  # 跟 api
        # 拿網址

        first_url = base_search_url + 'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(API_KEY,
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
        # data = video_links
        # return data
        return video_links
