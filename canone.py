from pathlib import Path
import soundfile as sf
import sounddevice as sd
import numpy as np
from math import sqrt
import random

directory = Path("outputs/freevc24.2025-12-21")

files = sorted(
    directory.glob("*.wav"),
    key=lambda p: int(p.stem.split("_")[1])
)

buffers = []
samplerate = None
start_offsets = []
pans = []

current_offset_sec = 0.0
overlap_delay = 3.0  # same as time.sleep(3)

for wav in files[100:110]:

    data, sr = sf.read(wav, dtype="float32")

    # force mono for panning
    if data.ndim == 2:
        data = data.mean(axis=1)

    samplerate = samplerate or sr

    buffers.append(data)
    start_offsets.append(int(current_offset_sec * samplerate))

    # 🔀 RANDOM PAN: -1 (left) → +1 (right)
    pan = random.uniform(-1.0, 1.0)
    pans.append(pan)

    print("queued", wav.name, "pan =", round(pan, 2))

    current_offset_sec += overlap_delay

# build final stereo mix buffer
total_length = max(
    offset + len(buf)
    for buf, offset in zip(buffers, start_offsets)
)

mix = np.zeros((total_length, 2), dtype=np.float32)

for buf, offset, pan in zip(buffers, start_offsets, pans):
    left = sqrt(0.5 * (1 - pan))
    right = sqrt(0.5 * (1 + pan))

    mix[offset : offset + len(buf), 0] += buf * left
    mix[offset : offset + len(buf), 1] += buf * right

# prevent clipping
peak = np.max(np.abs(mix))
if peak > 1.0:
    mix /= peak

# play once, let everything finish
sd.play(mix, samplerate)
sd.wait()