import os
from videodb import connect

os.environ["VIDEO_DB_API_KEY"] = "" # put your video_db api key

# connect to VideoDB
conn = connect()
coll = conn.get_collection('c-e69501a4-72ca-40c6-be37-bd1aee883221') # you can use these to get collection id and video id
videos = coll.get_videos()
print(videos)