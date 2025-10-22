# C Music Playlist (demo)

A minimal demo that shows how to:

1. Build a simple C CLI program (`playlist.c`)
2. Wrap it with Python UIs: Streamlit and Gradio

## Files
- `playlist.c` — simple in-memory playlist CLI
- `compile.sh` — compile script
- `app_streamlit.py` — Streamlit UI calling the C executable
- `app_gradio.py` — Gradio UI calling the C executable
- `requirements.txt` — Python dependencies

## Run locally (Linux / macOS)
1. Compile C:
   ```bash
   chmod +x compile.sh
   ./compile.sh
