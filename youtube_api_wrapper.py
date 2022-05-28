import json
import requests
from tqdm import tqdm
from video import video
from timestamp_manipulator import Timestamp
import data_reader as dr

class youtube_api:

    def __init__(self, api_key, channel_id, channel_name, limit):
        self.api_key = api_key
        self.channel_id = channel_id
        self.channel_name = channel_name
        self.videos = []
        self.limit = limit

    #extract all video information of the channel
    def get_channel_video_data(self):
        self._get_channel_content(self.limit)

    #extract all videos per channel
    def _get_channel_content(self, limit, check_all_pages=True):
        saved_data = dr.get_lines_amount(self.channel_name)
        if saved_data == 0:
            url = f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=snippet,id&order=date"
        else:
            timestamp = dr.read_data(0, 3, self.channel_name)
            timestamp_manipulator = Timestamp(str(timestamp))
            new_date = timestamp_manipulator.get_new_timestamp()
            url = f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=snippet,id&order=date&publishedAfter={new_date}"

        if limit is not None and isinstance(limit, int):
            url += "&maxResults=" + str(limit)

        npt = self._get_channel_content_per_page(url)
        idx = 0
        while(check_all_pages and npt is not None and idx < 10):
            nexturl = url + "&pageToken=" + npt
            npt = self._get_channel_content_per_page(nexturl)
            idx += 1

    #extracts all videos per page
    #returns nextPageToken
    def _get_channel_content_per_page(self, url):
        json_url = requests.get(url)
        data = json.loads(json_url.text)

        if 'items' not in data:
            print('Error! Could not get correct channel data!\n', data)
            return None

        nextPageToken = data.get("nextPageToken", None)

        item_data = data['items']
        for item in item_data:
            try:
                kind = item['id']['kind']
                published_at = item['snippet']['publishedAt']
                title = item['snippet']['title']
                if kind == 'youtube#video':
                    video_id = item['id']['videoId']
                    thumbnail = item["snippet"]["thumbnails"]["high"]["url"]
                    url = "https://www.youtube.com/watch?v=" + video_id
                    v = video(video_id, url, thumbnail, published_at, title)
                    self.videos.append(v)
            except KeyError as e:
                print('Error! Could not extract data from item:\n', item)

        return nextPageToken
