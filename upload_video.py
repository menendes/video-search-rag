import os
from videodb import connect

#set env variables
os.environ["VIDEO_DB_API_KEY"] = "" # put your video_db api key

# connect to VideoDB
conn = connect()
coll = conn.create_collection(
    name="cooking_tutorials", description="VideoDB Retrievers based on Cooking!", is_public=True
)

print(f"Collection ID: {coll.id}")

# upload videos to default collection in VideoDB
print("Uploading Video")
video = coll.upload(url="https://www.youtube.com/watch?v=JVrsw3GS92w") # you can replace the video url with yours
print(f"Video uploaded with ID: {video.id}")