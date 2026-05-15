import json
from beat.beat_point import beat_times

list_beat_times = beat_times.tolist()

with open("beats.json", "w") as f:
    json.dump(list_beat_times, f)