from videodb import connect
from videodb import SceneExtractionType
from llama_index.retrievers.videodb import VideoDBRetriever
from videodb import SearchType, IndexType
from llama_index.core import get_response_synthesizer
from videodb import play_stream
import time

conn = connect()
coll = conn.get_collection('c-3aadcc65-a560-4d4c-a474-09cf38254ad0') #replace with your collection id
video = coll.get_video('m-z-01955914-c134-7e92-bd1e-a59320b77dd9') # replace with your video id, you can also use get_videos to search multiple videos on the collections.

print("Indexing Spoken content in Video...")
video.index_spoken_words()

print("Indexing Visual content in Video...")
index_id = video.index_scenes(
    extraction_type=SceneExtractionType.shot_based,
    extraction_config={"frame_count": 3},
    prompt="Describe the cooking process in detail, mentioning ingredients, actions, and utensils used.",
)

scene_index = video.get_scene_index(index_id)

print(f"Scene Index successful with ID: {index_id}")

# Create retriever for spoken content
print("Retriever object created for spoken content")
spoken_retriever = VideoDBRetriever(
    collection=coll.id,
    video=video.id,
    search_type=SearchType.semantic,
    index_type=IndexType.spoken_word,
    score_threshold=0.1,
)

# create query for spoken content and retrieve the relevant timestamps
spoken_query = "How do I chop onions?"
nodes_spoken_index = spoken_retriever.retrieve(spoken_query)

# generating summarized response
print("Generating summarized response for spoken content")
response_synthesizer = get_response_synthesizer()
response = response_synthesizer.synthesize(
    spoken_query, nodes=nodes_spoken_index
)
print(f"Summarized Response: {response}")

print("Retriever object created for visual content")
scene_retriever = VideoDBRetriever(
    collection=coll.id,
    video=video.id,
    search_type=SearchType.semantic,
    index_type=IndexType.scene,
    scene_index_id=index_id,
    score_threshold=0.1,
)

# create query for spoken content and retrieve the relevant timestamps
scene_query = "Show me the part where onions are being chopped."
nodes_scene_index = scene_retriever.retrieve(scene_query)

# Retrieve video segments and merge them
print("Retrieving video segments and merging them for both spoken and visual search query")
spoken_results = [
    (node.metadata["start"], node.metadata["end"])
    for node in nodes_spoken_index
]

scene_results = [
    (node.metadata["start"], node.metadata["end"])
    for node in nodes_scene_index
]

# Merge timestamps from both retrievals
all_results = spoken_results + scene_results

stream_link = video.generate_stream(all_results)
time.sleep(3)
play_stream(stream_link)