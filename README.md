# Abandoned Project — Music Beat Visualizer

This was an attempt to build a music visualizer that reacts dynamically to the beat of a song in real-time.

The project was abandoned after running into several challenges.

## Why it was abandoned

- Difficulty detecting musically "interesting" moments (not just raw beats)
- Lack of experience with graphics libraries, making it hard to create nice visualizations
- The beat detection worked, but turning it into something visually appealing proved too difficult at the time

## Current State

Only the **beat detection** part currently works.

The project can successfully:
- Analyze an audio file (`music.mp3`)
- Detect beats using librosa
- Export the beat timestamps to a JSON file (`beats.json`)

## What currently works

### 1. Beat Detection (`beat_point.py`)

```python
import librosa

data, rate = librosa.load("music.mp3")
tempo, beat_frames = librosa.beat.beat_track(y=data, sr=rate)

print("Tempo:", tempo)
print("First 10 beat frames:", beat_frames[:10])

beat_times = librosa.frames_to_time(beat_frames, sr=rate)
print("First 5 beat times (seconds):", beat_times[:5])
```
### 2. Export beats to JSON (`save_bp.py`)

```python
import json
from beat.beat_point import beat_times   # assumes beat/ folder structure

list_beat_times = beat_times.tolist()

with open("beats.json", "w") as f:
    json.dump(list_beat_times, f)
```


Note: save_bp.py expects a folder structure like this:
project/
├── beat/
│   └── beat_point.py
├── save_bp.py
└── music.mp3
