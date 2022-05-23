import json
import requests
from tqdm import tqdm
from video import video

class youtube_api:

    def __init__(self, api_key, channel_id):
        self.api_key = api_key
        self.channel_id = channel_id
        self.video_data = None
        self.videos = []

    def get_channel_video_data(self):
        "Extract all video information of the channel"
        print('get video data...')
        channel_videos = self._get_channel_content(limit=1)

        part = "snippet"
        for video_id in tqdm(channel_videos):
                data = self._get_single_video_data(video_id, part)
                channel_videos[video_id].update(data)

        self.video_data = channel_videos
        return channel_videos

    def _get_single_video_data(self, video_id, part):
        """
        Extract further information for a single video
        parts can be: 'snippet', 'statistics', 'contentDetails', 'topicDetails'
        snippet - published at, title, thumbnails
        statistics - views, likes, comments count
        content details - duration
        """

        url = f"https://www.googleapis.com/youtube/v3/videos?part={part}&id={video_id}&key={self.api_key}"
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
            data = data['items'][0][part]
        except KeyError as e:
            print(f'Error! Could not get {part} part of data: \n{data}')
            data = dict()
        return data

    def _get_channel_content(self, limit, check_all_pages=True):
        """
        Extract all videos and playlists, can check all available search pages
        channel_videos = videoId: title, publishedAt
        channel_playlists = playlistId: title, publishedAt
        return channel_videos, channel_playlists
        """
        url = f"https://www.googleapis.com/youtube/v3/search?key={self.api_key}&channelId={self.channel_id}&part=snippet,id&order=date"

        if limit is not None and isinstance(limit, int):
            url += "&maxResults=" + str(limit)

        vid, npt = self._get_channel_content_per_page(url)
        idx = 0
        while(check_all_pages and npt is not None and idx < 10):
            nexturl = url + "&pageToken=" + npt
            next_vid, npt = self._get_channel_content_per_page(nexturl)
            vid.update(next_vid)
            idx += 1

        return vid

    def _get_channel_content_per_page(self, url):
        """
        Extract all videos and playlists per page
        return channel_videos, channel_playlists, nextPageToken
        """
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        channel_videos = dict()

        if 'items' not in data:
            print('Error! Could not get correct channel data!\n', data)
            return channel_videos, channel_videos, None

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
                    channel_videos[video_id] = {'publishedAt': published_at, 'title': title}
                    url = "https://www.youtube.com/watch?v=" + video_id
                    v = video(url, thumbnail, published_at, title)
                    self.videos.append(v)
            except KeyError as e:
                print('Error! Could not extract data from item:\n', item)

        return channel_videos, nextPageToken
