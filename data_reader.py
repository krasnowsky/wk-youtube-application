#			0		1			2				3		4
#position - id, video_url, thumbnail_url, timestamp, title
def read_data(video_number, position, channel_name):
    data_path = f'/Users/krasnowsky/wk_youtube/data/{channel_name}/videos.data'
    with open(data_path) as f:
        lines = f.readlines()
        return lines[video_number].split(';')[position]

def get_lines_amount(channel_name):
    with open(f'/Users/krasnowsky/wk_youtube/data/{channel_name}/videos.data', 'r') as fp:
        x = len(fp.readlines())
        return x