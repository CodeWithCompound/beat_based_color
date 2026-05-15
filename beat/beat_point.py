import librosa

data, rate = librosa.load("music.mp3")
tempo, beat_frames = librosa.beat.beat_track(y=data, sr=rate)

print("tempo:", tempo)
print("first 10 beat frames:", beat_frames[:10])

beat_times = librosa.frames_to_time(beat_frames, sr=rate)
print("first 5 beat times in seconds:", beat_times[:5])