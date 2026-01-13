# 🏥 Multi-Agent Medical Assistant

> An intelligent, AI-powered medical assistant that combines the best of language models, medical knowledge retrieval, web search, and computer vision to help analyze medical queries and images.

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Repository:** https://github.com/Saiesh04/MULTI-AGENT_MED-ASSISTANT

---

## 🌟 What is This Project?

Imagine having a medical assistant that can:
- **Answer medical questions** using both its knowledge base and up-to-date web information
- **Analyze medical images** like brain MRIs, chest X-rays, and skin lesions
- **Understand natural language** through speech-to-text capabilities
- **Speak responses back** using text-to-speech technology
- **Route your queries intelligently** to specialized agents based on what you're asking

This project brings together multiple AI agents, each with its own expertise, working together seamlessly to provide comprehensive medical assistance. It's built for researchers, medical students, and developers interested in AI-powered healthcare solutions.

---

## ✨ Key Features

### 🤖 Multi-Agent System
The system uses **LangGraph** to orchestrate multiple specialized agents:
- **💬 Conversation Agent**: Handles general medical discussions and patient queries
- **📚 RAG (Retrieval-Augmented Generation) Agent**: Searches through medical literature stored in a vector database
- **🌐 Web Search Agent**: Finds the latest medical information from PubMed and other sources
- **🧠 Brain Tumor Agent**: Analyzes MRI scans for brain tumor detection
- **🫁 Chest X-Ray Agent**: Detects COVID-19 and other abnormalities in chest X-rays
- **🔬 Skin Lesion Agent**: Segments and analyzes skin lesions from dermoscopic images

### 🛡️ Safety & Validation
- **Guardrails System**: Ensures responses meet safety and quality standards
- **Human-in-the-Loop**: Optional validation step for critical medical decisions
- Built-in content filtering to prevent harmful outputs

### 🎤 Voice Interaction
- **Speech-to-Text**: Upload audio recordings and get them transcribed (powered by ElevenLabs)
- **Text-to-Speech**: Convert text responses into natural-sounding speech

### 🎨 User-Friendly Interface
- Clean, intuitive web interface
- Real-time response streaming
- Image upload and analysis
- Session management for continuous conversations

---

## 🏗️ How It Works: System Architecture

The system uses an intelligent routing mechanism to direct your query to the most appropriate agent:

```
                                    👤 USER INPUT
                                         │
                                         ▼
                            ╔════════════════════════════╗
                            ║  🎯 AGENT DECISION SYSTEM  ║
                            ║   (Smart Query Router)     ║
                            ╚════════════════════════════╝
                                         │
                    ┌────────────────────┼────────────────────┐
                    │                    │                    │
        ┌───────────▼──────────┐  ┌─────▼──────┐  ┌─────────▼─────────┐
        │   💬 CONVERSATION    │  │  📚 RAG    │  │  🌐 WEB SEARCH    │
        │       AGENT          │  │   AGENT    │  │      AGENT        │
        │  (General Queries)   │  │ (Medical   │  │ (Latest News &    │
        │                      │  │Literature) │  │  Research)        │
        └──────────────────────┘  └────┬───┬───┘  └───────────────────┘
                                       │   │
                                       │   └─────────────┐
                                       │                 │
                                       │ Low Confidence? │
                                       │                 ▼
                                       │          🌐 Web Search
                                       │             (Fallback)
                                       │
        ┌──────────────────────────────┼──────────────────────────────┐
        │                              │                              │
        ▼                              ▼                              ▼
┌───────────────┐            ┌──────────────────┐           ┌────────────────┐
│  🧠 BRAIN     │            │  🫁 CHEST X-RAY  │           │  🔬 SKIN       │
│  TUMOR AGENT  │            │      AGENT       │           │  LESION AGENT  │
│  (MRI Scans)  │            │  (COVID/Normal)  │           │ (Segmentation) │
└───────┬───────┘            └────────┬─────────┘           └────────┬───────┘
        │                             │                              │
        └─────────────────────────────┼──────────────────────────────┘
                                      │
                                      ▼
                          ╔═══════════════════════╗
                          ║  ✅ HUMAN VALIDATION  ║
                          ║  (Critical Decisions) ║
                          ╚═══════════════════════╝
                                      │
                    ┌─────────────────┴─────────────────┐
                    │                                   │
                    ▼                                   ▼
        ┌───────────────────────┐         ┌────────────────────────┐
        │  Conversation Agent   │         │   Web Search Agent     │
        └───────────┬───────────┘         └────────────┬───────────┘
                    │                                  │
                    └──────────────┬───────────────────┘
                                   ▼
                        ╔══════════════════════╗
                        ║  🛡️ GUARDRAILS       ║
                        ║  (Safety & Quality)  ║
                        ╚══════════════════════╝
                                   │
                                   ▼
                        ╔══════════════════════╗
                        ║  📤 FINAL RESPONSE   ║
                        ║  (To User)           ║
                        ╚══════════════════════╝
```

### 🔄 The Workflow

1. **📥 Input Processing**: Your query or image is received through the web interface or API
2. **🎯 Smart Routing**: The Agent Decision system analyzes the input and routes it to the appropriate specialized agent
3. **🤖 Agent Processing**: The selected agent processes the request using its specialized models and knowledge
4. **✅ Validation**: For critical medical decisions, the system can request human validation
5. **🛡️ Safety Check**: Guardrails ensure the response meets safety and quality standards
6. **📤 Response Delivery**: The final, validated response is delivered to you

### 📁 Project Structure

```
multi-agent-medical-assistant/
├── 📄 app.py                    # Main FastAPI application
├── ⚙️ config.py                 # Configuration and settings
├── 🔧 ingest_rag_data.py        # Script to populate the knowledge base
├── 📦 requirements.txt          # Python dependencies
│
├── 🤖 agents/
│   ├── agent_decision.py        # Master orchestrator (LangGraph routing)
│   ├── guardrails/              # Safety and quality checks
│   ├── rag_agent/               # Medical literature search
│   ├── web_search_processor_agent/  # Web search capabilities
│   └── image_analysis_agent/    # Computer vision agents
│       ├── brain_tumor_agent/
│       ├── chest_xray_agent/
│       └── skin_lesion_agent/
│
├── 📊 data/
│   ├── raw/                     # Raw medical documents
│   ├── parsed_docs/             # Processed documents
│   └── qdrant_db/               # Vector database
│
├── 🖼️ sample_images/            # Test images
├── 🎨 templates/                # Web UI templates
└── 📤 uploads/                  # Runtime file uploads
```

---

## 🚀 Getting Started

### 📋 Prerequisites

Before you begin, make sure you have:

- **Python 3.10 or higher** - [Download here](https://www.python.org/downloads/)
- **FFmpeg** - Required for audio processing
  - **Windows**: `choco install ffmpeg` or [download manually](https://ffmpeg.org) and add to PATH
  - **macOS**: `brew install ffmpeg`
  - **Linux (Debian/Ubuntu)**: `sudo apt-get install ffmpeg`
- **(Optional) Docker** - If you prefer containerized deployment

### 🔧 Installation

#### Step 1: Clone the Repository

```bash
git clone https://github.com/Saiesh04/MULTI-AGENT_MED-ASSISTANT.git
cd MULTI-AGENT_MED-ASSISTANT
```

#### Step 2: Set Up Virtual Environment

Creating a virtual environment keeps your dependencies organized and prevents conflicts:

```bash
# Create virtual environment
python -m venv .venv

# Activate it
# On Windows:
.venv\Scripts\activate

# On macOS/Linux:
source .venv/bin/activate
```

#### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

This might take a few minutes as it installs all necessary packages including PyTorch, LangChain, FastAPI, and more.

#### Step 4: Configure Environment Variables

Create a `.env` file in the project root directory with your API keys:

```env
# 🔑 Google Gemini (Required for core functionality)
GOOGLE_API_KEY=your_google_api_key_here

# 🗄️ Qdrant Vector Database (Optional - defaults to local storage)
QDRANT_URL=
QDRANT_API_KEY=

# 🤗 Hugging Face (Optional - for some model pipelines)
HUGGINGFACE_TOKEN=

# 🔍 Tavily Web Search (Optional - for enhanced web search)
TAVILY_API_KEY=

# 🎤 ElevenLabs (Optional - for speech features)
ELEVEN_LABS_API_KEY=
```

**Important Notes:**
- **Google Gemini API Key** is essential - [Get it free here](https://makersuite.google.com/app/apikey)
- **Qdrant**: By default, uses local file storage at `./data/qdrant_db` (no cloud service needed)
- **Other keys**: Only needed if you want to use those specific features

#### Step 5: Prepare the Knowledge Base

Ingest medical documents into the vector database:

```bash
python ingest_rag_data.py
```

This script:
- Reads documents from the `data/raw/` folder
- Processes and chunks them intelligently
- Creates embeddings using Google's embedding model
- Stores them in the Qdrant vector database

**First run?** The process may take 5-10 minutes depending on the amount of data. Subsequent updates are faster!

#### Step 6: Download Medical AI Models

The project uses specialized deep learning models for image analysis:

**Chest X-Ray Model**: Already included at `agents/image_analysis_agent/chest_xray_agent/models/covid_chest_xray_model.pth` ✅

**Skin Lesion Model**: Download separately
```python
# Run this in Python
from agents.image_analysis_agent.skin_lesion_agent.model_download import download_model_checkpoint

download_model_checkpoint(
    gdrive_file_id="your_google_drive_file_id",
    output_path="agents/image_analysis_agent/skin_lesion_agent/models/checkpointN25_.pth.tar"
)
```

**Brain Tumor Model**: Place your model file at:
`agents/image_analysis_agent/brain_tumor_agent/models/brain_tumor_segmentation.pth`

> 💡 **Don't have these models?** The system will still work for text queries and chest X-rays!

---

## 🎮 Running the Application

### Option 1: Simple Start (Recommended)

```bash
python app.py
```

The server will start on `http://localhost:8000`

### Option 2: Development Mode (With Auto-Reload)

Perfect for development - automatically reloads when you modify code:

```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

### Option 3: Docker Container

Build and run using Docker:

```bash
# Build the image
docker build -t multi-agent-med-assistant .

# Run the container
docker run --rm -p 8000:8000 --env-file .env multi-agent-med-assistant
```

### ✅ Verify Installation

Open your browser and navigate to:
- **Web Interface**: http://localhost:8000
- **Health Check**: http://localhost:8000/health
- **API Documentation**: http://localhost:8000/docs (Interactive Swagger UI)

---

## 📖 Usage Guide

### 🌐 Using the Web Interface

1. Open your browser to http://localhost:8000
2. You'll see a clean, chat-like interface
3. **For Text Queries**: Simply type your medical question and press Enter
4. **For Image Analysis**: Click the upload button and select a medical image (MRI, X-Ray, or skin image)
5. **For Voice Input**: Click the microphone icon to record your question

### 🔌 Using the API

The system provides a RESTful API for programmatic access. Here are the main endpoints:

#### 1. 💬 Chat Endpoint

Send text-based medical queries:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the common symptoms of brain tumors?"
  }'
```

**Response:**
```json
{
  "response": "Common symptoms of brain tumors include...",
  "agent_used": "conversation",
  "confidence": 0.95,
  "sources": []
}
```

#### 2. 📤 Upload Image Endpoint

Analyze medical images:

```bash
curl -X POST http://localhost:8000/upload \
  -F "image=@path/to/chest_xray.jpg" \
  -F "text=Please analyze this chest X-ray for COVID-19"
```

**Supported Image Types:**
- 🧠 Brain MRI scans (.jpg, .png, .jpeg)
- 🫁 Chest X-rays (.jpg, .png, .jpeg)
- 🔬 Skin lesion images (.jpg, .png, .jpeg)

**Response:**
```json
{
  "analysis": "The chest X-ray shows...",
  "detected_condition": "COVID-19 Positive",
  "confidence": 0.87,
  "segmentation_image": "/uploads/skin_lesion_output/segmentation_plot.png",
  "requires_validation": true
}
```

#### 3. ✅ Validation Endpoint

For cases requiring human validation:

```bash
curl -X POST http://localhost:8000/validate \
  -F "validation_result=Yes" \
  -F "comments=The diagnosis appears accurate"
```

#### 4. 🎤 Speech-to-Text Endpoint

Transcribe medical audio recordings:

```bash
curl -X POST http://localhost:8000/transcribe \
  -F "audio=@recording.webm"
```

**Response:**
```json
{
  "transcript": "Patient complains of persistent headaches and dizziness"
}
```

#### 5. 🔊 Text-to-Speech Endpoint

Convert text responses to natural speech:

```bash
curl -X POST http://localhost:8000/generate-speech \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Your test results show normal values",
    "voice_id": "21m00Tcm4TlvDq8ikWAM"
  }'
```

Returns an audio file (mp3 format) that can be played back.

---

## 💡 Example Use Cases

### Example 1: General Medical Question

**Query:** "What are the early signs of diabetes?"

**What Happens:**
1. Agent Decision routes to **Conversation Agent** or **RAG Agent**
2. System searches medical literature in the vector database
3. Guardrails check the response for accuracy and safety
4. Response delivered with citations

---

### Example 2: Analyzing a Chest X-Ray

**Input:** Upload chest X-ray image + "Check for COVID-19"

**What Happens:**
1. Agent Decision identifies this as a chest X-ray analysis task
2. Routes to **Chest X-Ray Agent**
3. Deep learning model analyzes the image
4. Returns classification (COVID-positive/Normal) with confidence score
5. May request human validation if confidence is below threshold

---

### Example 3: Latest Medical News

**Query:** "What are the latest treatments for Alzheimer's disease?"

**What Happens:**
1. Agent Decision recognizes need for current information
2. Routes to **Web Search Agent**
3. Searches PubMed and medical news sources
4. Aggregates and summarizes findings
5. Provides cited sources

---

### Example 4: Skin Lesion Analysis

**Input:** Upload dermoscopic image + "Is this melanoma?"

**What Happens:**
1. Routes to **Skin Lesion Agent**
2. Performs segmentation to identify the lesion boundaries
3. Analyzes features and patterns
4. Provides assessment with visualization
5. **Always** requests human (dermatologist) validation

---

## 🎯 Advanced Configuration

### Customizing Agent Behavior

Edit `config.py` to customize:

```python
class Config:
    class RAG:
        use_local = True  # Use local Qdrant vs cloud
        collection_name = "medical_docs"
        chunk_size = 1000
        chunk_overlap = 200
        top_k = 5  # Number of documents to retrieve
    
    class Models:
        decision_model = "gemini-2.5-flash"
        vision_model = "gemini-2.5-flash"
        embedding_model = "models/text-embedding-004"
    
    class Speech:
        enabled = True  # Enable/disable speech features
        voice_id = "21m00Tcm4TlvDq8ikWAM"  # ElevenLabs voice
```

### Adding Your Own Medical Documents

1. Place documents (PDF, TXT, DOCX) in `data/raw/`
2. Run the ingestion script:
   ```bash
   python ingest_rag_data.py
   ```
3. Documents are automatically chunked, embedded, and indexed

### Adjusting Guardrails

Modify `agents/guardrails/local_guardrails.py` to customize:
- Content filtering rules
- Confidence thresholds
- Safety checks
- Response validation criteria

---

## 🔧 Troubleshooting

### Common Issues and Solutions

#### Issue: "Module not found" errors
**Solution:** Make sure you've activated your virtual environment and installed all dependencies:
```bash
# Activate virtual environment
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

#### Issue: FFmpeg not found
**Solution:** Install FFmpeg and ensure it's in your system PATH:
- Windows: Download from [ffmpeg.org](https://ffmpeg.org) and add to PATH
- macOS: `brew install ffmpeg`
- Linux: `sudo apt-get install ffmpeg`

#### Issue: "GOOGLE_API_KEY not found"
**Solution:** Make sure your `.env` file exists in the project root and contains a valid API key:
```env
GOOGLE_API_KEY=your_actual_api_key_here
```

#### Issue: Image analysis not working
**Solution:** Verify that the required model files are in place:
- Chest X-ray: `agents/image_analysis_agent/chest_xray_agent/models/covid_chest_xray_model.pth`
- Skin lesion: `agents/image_analysis_agent/skin_lesion_agent/models/checkpointN25_.pth.tar`
- Brain tumor: `agents/image_analysis_agent/brain_tumor_agent/models/brain_tumor_segmentation.pth`

#### Issue: Qdrant connection errors
**Solution:** If using local mode (default), no connection needed. If using cloud:
- Verify `QDRANT_URL` and `QDRANT_API_KEY` in `.env`
- Check network connectivity
- Try switching to local mode in `config.py`

#### Issue: Windows line ending warnings (CRLF)
**Solution:** Configure Git to handle line endings:
```powershell
git config core.autocrlf true
```

---

## 🗂️ Data & Model Files

### Sample Images Included

Test the system with included sample images:

**Chest X-Rays:**
- Location: `sample_images/chest_x-ray_covid_and_normal/`
- Contains: COVID-positive and normal chest X-rays
- Format: JPG

**Skin Lesions:**
- Location: `sample_images/skin_lesion_images/`
- Contains: Various dermoscopic images
- Format: JPG/PNG

### Upload Directories

During runtime, files are organized in:

| Directory | Purpose |
|-----------|---------|
| `uploads/backend/` | Backend processed uploads |
| `uploads/frontend/` | Frontend user uploads |
| `uploads/skin_lesion_output/` | Segmentation visualizations |
| `uploads/speech/` | Temporary audio files |

### Vector Database

**Local Mode (Default):**
- Location: `data/qdrant_db/`
- No external service required
- Automatically created on first run

**Cloud Mode:**
- Requires Qdrant cloud account
- Configure via `QDRANT_URL` and `QDRANT_API_KEY`

---

## 🧠 Understanding the AI Models

### Language Models (Google Gemini)

**Gemini 2.5 Flash:**
- Used for: Quick decision-making, routing queries
- Strengths: Fast, cost-effective, good for classification
- Context window: 1M tokens

**Text Embeddings:**
- Model: `text-embedding-004`
- Dimension: 768
- Used for: Converting text to vectors for similarity search

### Computer Vision Models

**Chest X-Ray Classifier:**
- Architecture: Custom CNN
- Classes: COVID-19 Positive, Normal
- Input: 224x224 RGB images
- Output: Classification + confidence score

**Skin Lesion Segmentation:**
- Architecture: U-Net based
- Task: Pixel-wise segmentation
- Output: Segmentation mask + visualization

**Brain Tumor Detector:**
- Architecture: ResNet-based
- Task: Tumor detection and classification
- Input: MRI scans

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **🐛 Report Bugs**: Open an issue describing the bug and how to reproduce it
2. **💡 Suggest Features**: Share your ideas for new features or improvements
3. **📝 Improve Documentation**: Help make the docs clearer and more comprehensive
4. **🔧 Submit Pull Requests**: Fix bugs or implement new features

### Development Setup

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes
4. Write tests if applicable
5. Commit with clear messages: `git commit -m "Add feature X"`
6. Push to your fork: `git push origin feature-name`
7. Open a Pull Request

### Code Style

- Follow PEP 8 for Python code
- Add docstrings to functions and classes
- Keep functions focused and modular
- Write clear commit messages

---

## 📚 Technical Stack

| Component | Technology |
|-----------|-----------|
| **Backend Framework** | FastAPI |
| **AI Orchestration** | LangGraph, LangChain |
| **Language Models** | Google Gemini 2.5 Flash |
| **Embeddings** | Google text-embedding-004 |
| **Vector Database** | Qdrant |
| **Computer Vision** | PyTorch, OpenCV |
| **Web Search** | Tavily, PubMed API |
| **Speech Processing** | ElevenLabs |
| **Frontend** | HTML, JavaScript, Bootstrap |
| **Containerization** | Docker |

---

## 📜 API Reference

### Complete Endpoint List

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Web UI homepage |
| `GET` | `/health` | Health check endpoint |
| `GET` | `/docs` | Interactive API documentation (Swagger) |
| `POST` | `/chat` | Submit text query |
| `POST` | `/upload` | Upload and analyze medical image |
| `POST` | `/validate` | Submit human validation result |
| `POST` | `/transcribe` | Convert audio to text |
| `POST` | `/generate-speech` | Convert text to speech |

### Request/Response Schemas

See interactive documentation at `http://localhost:8000/docs` for detailed schemas with examples.

---

## 🎓 Educational Resources

Want to learn more about the technologies used?

- **LangGraph**: [Documentation](https://langchain-ai.github.io/langgraph/)
- **Google Gemini**: [API Guide](https://ai.google.dev/docs)
- **FastAPI**: [Tutorial](https://fastapi.tiangolo.com/tutorial/)
- **Qdrant**: [Getting Started](https://qdrant.tech/documentation/)
- **Medical AI**: [Papers With Code - Medical Imaging](https://paperswithcode.com/area/medical)

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## ⚠️ Important Disclaimer

**THIS SOFTWARE IS FOR EDUCATIONAL AND RESEARCH PURPOSES ONLY**

🚨 **Critical Notice:**
- This project is **NOT** a medical device
- It does **NOT** provide medical advice, diagnosis, or treatment
- Results should **NEVER** be used as a substitute for professional medical advice
- **Always consult** qualified healthcare professionals for medical decisions
- The developers assume **NO LIABILITY** for any medical decisions made using this software

**Regulatory Compliance:**
- Not FDA approved
- Not CE marked
- Not intended for clinical use
- Not validated for diagnostic purposes

**Use Cases:**
- ✅ Research and development
- ✅ Educational demonstrations
- ✅ Proof-of-concept projects
- ✅ AI/ML experimentation
- ❌ Clinical diagnosis
- ❌ Patient care
- ❌ Treatment decisions

---

## 🙏 Acknowledgements

This project stands on the shoulders of giants. Special thanks to:

### Technologies & Frameworks
- **LangChain & LangGraph** - For the multi-agent orchestration framework
- **Google AI** - For Gemini models and embeddings
- **Qdrant** - For the powerful vector database
- **FastAPI** - For the modern, fast web framework
- **PyTorch** - For deep learning capabilities
- **ElevenLabs** - For natural speech synthesis
- **Tavily** - For intelligent web search

### Data & Research
- **PubMed/NCBI** - For access to medical literature
- **Medical Research Community** - For open datasets
- See `agents/README.md` for specific citations and data sources used in the RAG agent

### Open Source Community
- All the amazing developers who contribute to open-source AI/ML libraries
- The Python community for exceptional tooling and documentation

---

## 📧 Contact & Support

- **GitHub Issues**: [Report bugs or request features](https://github.com/Saiesh04/MULTI-AGENT_MED-ASSISTANT/issues)
- **Repository**: [Saiesh04/MULTI-AGENT_MED-ASSISTANT](https://github.com/Saiesh04/MULTI-AGENT_MED-ASSISTANT)
- **Discussions**: Use GitHub Discussions for questions and community interaction

---

## 🔮 Roadmap & Future Enhancements

Potential future improvements:

- [ ] Support for additional medical imaging modalities (CT, ultrasound)
- [ ] Multi-language support for international users
- [ ] Integration with Electronic Health Records (EHR) systems
- [ ] Real-time collaborative diagnosis sessions
- [ ] Mobile application for on-the-go access
- [ ] Enhanced privacy features (HIPAA compliance considerations)
- [ ] Federated learning capabilities for privacy-preserving model updates
- [ ] Integration with wearable device data

Want to contribute to these features? Check out our [Contributing](#-contributing) section!

---

## 📊 Performance & Metrics

### System Requirements

**Minimum:**
- CPU: 4 cores
- RAM: 8GB
- Storage: 10GB
- Internet: Required for API calls

**Recommended:**
- CPU: 8+ cores
- RAM: 16GB+
- GPU: NVIDIA GPU with 8GB+ VRAM (for faster image processing)
- Storage: 20GB SSD

### Response Times (Approximate)

| Operation | Typical Time |
|-----------|--------------|
| Text query (simple) | 1-3 seconds |
| RAG search | 2-5 seconds |
| Web search | 5-10 seconds |
| Chest X-ray analysis | 3-7 seconds |
| Skin lesion segmentation | 5-10 seconds |
| Brain MRI analysis | 5-10 seconds |

*Times vary based on hardware, network, and query complexity*

---

<div align="center">

### ⭐ If you find this project helpful, please consider giving it a star!

**Built with ❤️ for the advancement of medical AI**

[🏠 Back to Top](#-multi-agent-medical-assistant)

</div>
