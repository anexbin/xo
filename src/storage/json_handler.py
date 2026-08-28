import json
from pathlib import Path
from dataclasses import asdict
from ..models.track import Track

DATA_FILE = Path(__file__).parent.parent.parent / "data" / "tracks.json"

def load_tracks():
    if not DATA_FILE.exists():
        return []
    
    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        
        tracks = [Track(**item) for item in data]
        return tracks
    
    except json.JSONDecodeError:
        print("Warning: tracks.json is corrupted. Starting fresh.")
        return []

def save_tracks(tracks):
    data = [asdict(track) for track in tracks]
    
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)
    
    print(f"Saved {len(tracks)} songs to tracks.json")
