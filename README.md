# **Multimodal Video Search Engine** 🎥🔍  

This project implements a **video search mechanism** using `llama-index`, `videodb`, and `llama-index-retrievers-videodb`. It enables **multimodal search**, allowing users to search for **spoken content** and **visual scenes** within a video using **semantic queries**.

---

## **Project Scenario**  

Imagine watching a **cooking tutorial** and needing to quickly find:  
✅ The **exact moment** where the chef chops onions.  
✅ The **spoken instructions** for adding spices.  
✅ A **concise summary** of the cooking process.  

With this project, you can **search using natural language queries**, and the system will retrieve **the most relevant video segments**, letting you **watch only the necessary parts** instead of manually scrubbing through the entire video.

---

## **How It Works**  
1. **Indexing**  
   - Spoken content is **transcribed and indexed** for semantic search.  
   - Visual content is **segmented into scenes** for retrieval.  

2. **Retrieval**  
   - Users can **search by text queries** (e.g., "How do I chop onions?")  
   - The system finds **spoken instructions** and **matching video scenes**.  

3. **Streaming**  
   - The retrieved video segments are **played instantly**, showing only the relevant portions.  

---




## **Installation**
1. **Create and activate a Conda environment:**
   ```sh
   conda create --name video-search
   conda activate video-search
2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
