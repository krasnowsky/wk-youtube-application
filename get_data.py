from turtle import down
from urllib import response
from youtube_api_wrapper import youtube_api
import data_reader as dr
import config_parser
import requests
import os

class Data:

	def __init__(self):
		self.API_KEY = config_parser.api_key

		self.channel_names = ['ekipa_wk', 'wk_dzik_pl', 'warszawski_koks', 'kuchnia_wk', 'wk_gaming']
		self.channel_ids = ['UCnvrd6z-UgyX0n-Db7sQI4Q', 'UCUr1w6sHtgj1JniKV8vWXMw', 'UC2AyohFiDUS3K98h5dJVfog', 'UC4TYJ_RcqwL9lAZgkQlk11g', 'UCeLWHfuhwnObampm0M6oH4w']

	def download_thumbnail(url, video_id, channel_name):
		response = requests.get(url)
		path = f'/Users/krasnowsky/wk_youtube/data/{channel_name}/thumbnails/{video_id}.png'
		file = open(path, 'wb')
		file.write(response.content)
		file.close()

	def write_data(video, channel_name, flag):
		path = f'/Users/krasnowsky/wk_youtube/data/{channel_name}/videos.data'
		line = f'{video.id};{video.url};{video.thumbnail};{video.published_at};{video.title}\n'
		if flag:
			file = open(path, "a")
			file.write(line)
			file.close()
		else:
			with open(path, 'r+') as file:
				content = file.read()
				file.seek(0)
				file.write(line + content)

	def get_data(self):
		for i in range(5):
			data = youtube_api(self.API_KEY, self.channel_ids[i], self.channel_names[i], 1)
			data.get_channel_video_data()

			if len(data.videos) != 0:
				if_file_empty = True
				videos_in_file = dr.get_lines_amount(self.channel_names[i])
				if videos_in_file != 0:
					if_file_empty = False

				videos_ids = []

				for line_number in range(videos_in_file):
					videos_ids[line_number] = dr.read_data(line_number, 0, self.channel_names[i])

				for vid in data.videos:
					if vid.id not in videos_ids:
						self.download_thumbnail(vid.thumbnail, vid.id, self.channel_names[i])
						self.write_data(vid, self.channel_names[i], if_file_empty)
			else:
				print(f"No new videos found on {self.channel_names[i]}")

data = Data()
data.get_data()


