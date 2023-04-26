# 1. get all video list from a channel
from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.pipeline import Pipeline

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'  # global 的話用全大寫來示意内容不變


def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        GetVideoList(),
    ]

    p = Pipeline(steps)
    p.run(inputs)


if __name__ == '__main__':  # 多寫個 check 來確認程式進入點是從檔案 main 的位置, 以防其它 import 的 function 裡也有 main 的執行檔
    main()

# 2. download youtube subtitle
# 3. download youtube video
# 4. edit video
