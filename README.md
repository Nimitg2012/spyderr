# SPydeRR - Smart Personal Interactive Digital Entity for Response

SPydeRR is a voice-controlled Python assistant with fun, intelligence, and web-connected features.

## Features
- Voice-controlled commands
- Tells jokes, weather, time, date
- Translates text using Deep Translator
- Plays YouTube songs
- Google search
- Fun spider-themed Easter eggs

## Setup Instructions

1. **Clone/Download SPydeRR**

2. **Navigate into folder:**
```bash
cd spyderr_project
```

3. **Create and activate virtual environment (Mac):**
```bash
python3 -m venv spyderr-venv
source spyderr-venv/bin/activate
```

4. **Install dependencies:**
```bash
pip install -r requirements.txt
```

5. **Run the assistant:**
```bash
python spyderr.py
```

> Note: Make sure `pyaudio` is installed correctly. On Mac with Homebrew:
```bash
brew install portaudio
pip install pyaudio
```
### 6. Set Your SerpAPI Key
Export your key as an environment variable:

```bash
export SERPAPI_API_KEY='your_api_key_here'
```

## Author
SPydeRR by Nimit Mahajan
