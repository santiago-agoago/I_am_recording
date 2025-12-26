import soundfile as sf
import sounddevice as sd
import numpy as np
from pathlib import Path
from math import sqrt
import random

directory = Path("outputs/freevc24.2025-12-21")

files = sorted(
    directory.glob("*.wav"),
    key=lambda p: int(p.stem.split("_")[1])
)

buffers = []
samplerate = None
pans = []

for wav in files[:99]:
    data, sr = sf.read(wav, dtype="float32")

    # force mono for panning
    if data.ndim == 2:
        data = data.mean(axis=1)

    samplerate = samplerate or sr
    buffers.append(data)

    # 🔀 random pan per file
    pans.append(random.uniform(-1.0, 1.0))

# pad to same length
max_len = max(len(b) for b in buffers)
buffers = [
    np.pad(b, (0, max_len - len(b)))
    for b in buffers
]

# stereo mix
mix = np.zeros((max_len, 2), dtype=np.float32)

for buf, pan in zip(buffers, pans):
    left = sqrt(0.5 * (1 - pan))
    right = sqrt(0.5 * (1 + pan))

    mix[:, 0] += buf * left
    mix[:, 1] += buf * right

# prevent clipping
peak = np.max(np.abs(mix))
if peak > 1.0:
    mix /= peak

sd.play(mix, samplerate)
sd.wait()
