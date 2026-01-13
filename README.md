# MULTI-AGENT MED-ASSISTANT

A FastAPI-based multi-agent medical assistant that combines LLM reasoning (Google Gemini), Retrieval-Augmented Generation (RAG) over medical literature (Qdrant vector store), web search processing, and medical computer vision agents (brain tumor, chest X-ray, skin lesion). Includes a minimal web UI, optional speech transcription and TTS using ElevenLabs, and human-in-the-loop validation.

Repo: https://github.com/Saiesh04/MULTI-AGENT_MED-ASSISTANT

---

## Features
- Multi-agent routing with LangGraph
  - Conversation agent, RAG agent, Web Search Processor agent
  - Medical CV agents: Brain Tumor, Chest X-ray (COVID/Normal), Skin Lesion segmentation
- Guardrails + optional human validation flow
- RAG over local docs with Qdrant (local folder by default)
- Google Gemini chat + embeddings
- Lightweight web UI served from FastAPI templates
- Optional speech: transcription and TTS via ElevenLabs

---

## Architecture (high level)
```mermaid
flowchart LR
  A[User] -->|/chat or /upload| D[Agent Decision]
  D -->|text| C[Conversation]
  D -->|knowledge| R[RAG]
  D -->|news/time-sensitive| W[Web Search Processor]
  D -->|image (brain MRI)| B[Brain Tumor Agent]
  D -->|image (CXR)| X[Chest X-ray Agent]
  D -->|image (skin)| S[Skin Lesion Agent]
  B --> V[Human Validation]
  X --> V
  S --> V
  R -->|low confidence or insufficient info| W
  V --> G[Guardrails]
  C --> G
  W --> G
  G --> U[Response]
```

Key code:
- `app.py`: FastAPI app, routes, UI, speech endpoints
- `config.py`: All configuration and model choices
- `agents/agent_decision.py`: Orchestration and routing with LangGraph
- `agents/`: Agent implementations (RAG, web-search, CV, guardrails)
- `templates/index.html`: Minimal front-end

---

## Prerequisites
- Python 3.10+
- FFmpeg (required by pydub)
  - Windows: `choco install ffmpeg` or download from ffmpeg.org and add to PATH
  - macOS: `brew install ffmpeg`
  - Linux (Debian/Ubuntu): `sudo apt-get install ffmpeg`
- (Optional) Docker

---

## Setup
1) Create and activate a virtual environment
```bash
python -m venv .venv
# Windows
. .venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
```

2) Install dependencies
```bash
pip install -r requirements.txt
```

3) Environment variables (.env)
Create a `.env` file in the project root with the following keys (adjust as needed):
```env
# Google Gemini
GOOGLE_API_KEY=your_google_api_key

# Qdrant (optional if using local, which is default)
QDRANT_URL=
QDRANT_API_KEY=

# Hugging Face (optional; used by some pipelines)
HUGGINGFACE_TOKEN=

# Web search (optional)
TAVILY_API_KEY=

# ElevenLabs (optional; for speech)
ELEVEN_LABS_API_KEY=
```
Notes:
- By default, RAG uses a local Qdrant folder at `./data/qdrant_db` (`Config.rag.use_local=True`).
- If you use a managed Qdrant instance, fill `QDRANT_URL` and `QDRANT_API_KEY`.

4) (Recommended) Ingest sample documents for RAG
```bash
python ingest_rag_data.py
```
This builds/updates the local vector DB in `data/qdrant_db/`.

---

## Running the app
- Option A (simple):
```bash
python app.py
```
- Option B (dev auto-reload):
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```
Visit: http://localhost:8000

Health check: `GET /health`

---

## API summary
- `GET /` — Web UI
- `GET /health` — Liveness check
- `POST /chat` — JSON body: `{ "query": "text" }`
- `POST /upload` — multipart: `image` (png/jpg/jpeg) + optional `text`
- `POST /validate` — form: `validation_result` (Yes/No), `comments` (optional)
- `POST /transcribe` — multipart: `audio` (webm) → transcript (requires ELEVEN_LABS_API_KEY)
- `POST /generate-speech` — JSON: `{ "text": "...", "voice_id": "..." }` → mp3 (requires ELEVEN_LABS_API_KEY)

Example: Chat
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"query":"What are common symptoms of brain tumors?"}'
```

Example: Image upload
```bash
curl -X POST http://localhost:8000/upload \
  -F "image=@sample_images/chest_x-ray_covid_and_normal/covid-example-01.jpg" \
  -F "text=please analyze"
```

---

## Models and assets
- Chest X-ray model: `agents/image_analysis_agent/chest_xray_agent/models/covid_chest_xray_model.pth` (included)
- Skin Lesion segmentation checkpoint path (expected):
  `agents/image_analysis_agent/skin_lesion_agent/models/checkpointN25_.pth.tar`
  - You can download it with the helper:
    ```python
    # agents/image_analysis_agent/skin_lesion_agent/model_download.py
    from agents.image_analysis_agent.skin_lesion_agent.model_download import download_model_checkpoint

    download_model_checkpoint(
        gdrive_file_id="<your_google_drive_file_id>",
        output_path="agents/image_analysis_agent/skin_lesion_agent/models/checkpointN25_.pth.tar",
    )
    ```
- Brain Tumor model path (expected):
  `agents/image_analysis_agent/brain_tumor_agent/models/brain_tumor_segmentation.pth`
  - Place your model at this path if you plan to use this agent.

Sample images:
- `sample_images/chest_x-ray_covid_and_normal/`
- `sample_images/skin_lesion_images/`

Uploads (runtime):
- Backend uploads: `uploads/backend/`
- Frontend uploads: `uploads/frontend/`
- Skin lesion output: `uploads/skin_lesion_output/segmentation_plot.png`
- Speech temp files: `uploads/speech/`

---

## Docker (optional)
Build and run (will expose on 8000):
```bash
docker build -t multi-agent-med-assistant .
docker run --rm -p 8000:8000 --env-file .env multi-agent-med-assistant
```

---

## Windows line endings (optional)
If you see CRLF warnings, you can configure:
```powershell
git config core.autocrlf true
```

---

## Disclaimer
This project is for research/education. It is NOT a medical device and does NOT provide medical advice or diagnosis. Always consult licensed healthcare professionals.

---

## Acknowledgements
- LangChain, LangGraph, Qdrant
- Google Gemini
- ElevenLabs
- See `agents/README.md` for citations used by the RAG agent.
