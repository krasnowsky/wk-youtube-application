from helper import YTstats

API_KEY = "AIzaSyC8wCMk2lHAnlovlw_5fjl1fm03IJRmh80"
ekipa_wk_id = 'UCnvrd6z-UgyX0n-Db7sQI4Q'
channel_id = ekipa_wk_id

yt = YTstats(API_KEY, channel_id)
yt.extract_all()
print(yt.videos)
#yt.dump()  # dumps to .json