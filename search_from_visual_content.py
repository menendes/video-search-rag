from videodb import connect
from videodb import SceneExtractionType
from llama_index.retrievers.videodb import VideoDBRetriever
from videodb import SearchType, IndexType
from llama_index.core import get_response_synthesizer
from videodb import play_stream

conn = connect()
coll = conn.get_collection('c-17bf1180-447d-4097-8ce0-851e0f3d8b10') #replace with your collection id
video = coll.get_video('m-z-01954470-5c89-7a81-b49a-e0d37c3d07ee') # replace with your video id, you can also use get_videos to search multiple videos on the collections.

print("Indexing Visual content in Video...")

# Index scene content
index_id = video.index_scenes(
    extraction_type=SceneExtractionType.shot_based,
    extraction_config={"frame_count": 3},
    prompt="Describe the scene in detail",
)

scene_index = video.get_scene_index(index_id)

print(f"Scene Index successful with ID: {index_id}")

scene_retriever = VideoDBRetriever(
    collection=coll.id,
    video=video.id,
    search_type=SearchType.semantic,
    index_type=IndexType.scene,
    scene_index_id=index_id,
    score_threshold=0.1,
)

scene_query = "Find clips where the lead singer is interacting with the audience"
nodes_scene_index = scene_retriever.retrieve(scene_query)

#viewing result as text
response_synthesizer = get_response_synthesizer()
response = response_synthesizer.synthesize(
    scene_query, nodes=nodes_scene_index
)
print(response)

#viewing the result as video clip
results = [
    (node.metadata["start"], node.metadata["end"])
    for node in nodes_scene_index
]

stream_link = video.generate_stream(results)
play_stream(stream_link)