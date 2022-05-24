from helper import youtube_api
import config_parser
import requests
import os

API_KEY = config_parser.api_key
ekipa_wk_id = 'UCnvrd6z-UgyX0n-Db7sQI4Q'
wk_dzik_pl_id = 'UCUr1w6sHtgj1JniKV8vWXMw'
warszawski_koks_id = 'UC2AyohFiDUS3K98h5dJVfog'
kuchnia_wk_id = 'UC4TYJ_RcqwL9lAZgkQlk11g'
wk_gaming_id = 'UCeLWHfuhwnObampm0M6oH4w'

channel_names = ['ekipa_wk', 'wk_dzik_pl', 'warszawski_koks', 'kuchnia_wk', 'wk_gaming']
channel_ids = ['UCnvrd6z-UgyX0n-Db7sQI4Q', 'UCUr1w6sHtgj1JniKV8vWXMw', 'UC2AyohFiDUS3K98h5dJVfog', 'UC4TYJ_RcqwL9lAZgkQlk11g', 'UCeLWHfuhwnObampm0M6oH4w']

channels = {
  "ekipa_wk": 'UCnvrd6z-UgyX0n-Db7sQI4Q',
  "wk_dzik_pl": 'UCUr1w6sHtgj1JniKV8vWXMw',
  "warszawski_koks": 'UC2AyohFiDUS3K98h5dJVfog',
  "kuchnia_wk": 'UC4TYJ_RcqwL9lAZgkQlk11g',
  "wk_gaming": 'UCeLWHfuhwnObampm0M6oH4w'
}

for i in range(5):
    data = youtube_api(API_KEY, channel_ids[i], 1)
    data.get_channel_video_data()

    path = f'/Users/krasnowsky/wk_youtube/data/{channel_names[i]}/thumbnails/'
    thumbnails_downloaded = os.listdir(path)

    path_1 = f'/Users/krasnowsky/wk_youtube/data/{channel_names[i]}/videos.data'


    for vid in data.videos:
        '''if vid.id + '.png' not in thumbnails_downloaded:
        response = requests.get(vid.thumbnail)
        path = f'/Users/krasnowsky/wk_youtube/data/{channel_names[i]}/thumbnails/{vid.id}.png'

        file = open(path, "wb")
        file.write(response.content)
        file.close()
'''
        data_file = open(path_1, "a")
        data_file.write(f'{vid.id};{vid.url};{vid.thumbnail};{vid.published_at};{vid.title}\n')
        data_file.close()


