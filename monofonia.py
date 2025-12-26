import soundfile as sf
import sounddevice as sd
import numpy as np
from pathlib import Path

directory = Path("outputs/freevc24.2025-12-21")

files = sorted(
    directory.glob("*.wav"),
    key=lambda p: int(p.stem.split("_")[1])
)

buffers = []
samplerate = None

for wav in files[100:199]:
    data, sr = sf.read(wav, dtype="float32")
    samplerate = samplerate or sr
    buffers.append(data)

# pad to same length
max_len = max(len(b) for b in buffers)
buffers = [
    np.pad(b, (0, max_len - len(b)))
    for b in buffers
]

# mix (prevent clipping!)
mix = np.sum(buffers, axis=0)
mix /= max(np.max(np.abs(mix)), 1.0)

sd.play(mix, samplerate)
sd.wait()
