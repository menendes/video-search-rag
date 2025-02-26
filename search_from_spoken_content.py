from videodb import connect
from llama_index.retrievers.videodb import VideoDBRetriever
from videodb import SearchType, IndexType
from llama_index.core import get_response_synthesizer
from videodb import play_stream

conn = connect()
coll = conn.get_collection('c-e69501a4-72ca-40c6-be37-bd1aee883221') #replace with your collection id
video = coll.get_video('m-z-0195440d-b4be-7be3-8b47-cc483fd42ea7') # replace with your video id, you can also use get_videos to search multiple videos on the collections.

#video.index_spoken_words() #skip it once you implement

spoken_retriever = VideoDBRetriever(
    collection=coll.id,
    video=video.id,
    search_type=SearchType.semantic,
    index_type=IndexType.spoken_word,
    score_threshold=0.1,
)

spoken_query = "What is the content of this video?"
nodes_spoken_index = spoken_retriever.retrieve(spoken_query)

response_synthesizer = get_response_synthesizer()

response = response_synthesizer.synthesize(
    spoken_query, nodes=nodes_spoken_index
)
print(response)

results = [
    (node.metadata["start"], node.metadata["end"])
    for node in nodes_spoken_index
]

stream_link = video.generate_stream(results)
play_stream(stream_link)