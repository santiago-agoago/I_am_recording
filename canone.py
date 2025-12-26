from pathlib import Path
import simpleaudio as sa
import time

directory = Path("outputs/freevc24.2025-12-21")

# sem o sorted() os arquivos não são reproduzidos em ordem alfabética, mas na ordem do sistema de organização de arquivos do sistema operacional. o resultado semi-aleatório é interessante
files = sorted(
    directory.glob("*.wav"),
    key=lambda p: int(p.stem.split("_")[1])
)

playbacks = []

for wav in files[100:110]:
    if wav.name == 'conversion_100.wav':
        break

    wave_obj = sa.WaveObject.from_wave_file(str(wav))
    play_obj = wave_obj.play()

    # foi o chatgpt
    playbacks.append(play_obj)

    print("playing", wav.name)
    time.sleep(3)   # intentional overlap

# wait until *all* sounds finish
for play_obj in playbacks:
    play_obj.wait_done()
