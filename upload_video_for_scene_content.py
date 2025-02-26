import os
from videodb import connect

#set env variables
os.environ["VIDEO_DB_API_KEY"] = "" # put your video_db api key

# connect to VideoDB
conn = connect()
coll = conn.create_collection(
    name="video-search-scene-index-poc", description="VideoDB Retrievers", is_public=True
)

# upload videos to default collection in VideoDB
print("Uploading Video")
video = coll.upload(url="https://www.youtube.com/watch?v=CePKiLm6Pk4") # you can replace the video url with yours
print(f"Video uploaded with ID: {video.id}")