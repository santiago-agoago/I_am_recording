import os
import datetime
from uniqpath import unique_path
from TTS.api import TTS
from pathlib import Path


def dir_diario(tipo):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    dir_nome = f"{tipo}.{now}"

    output_dir = Path.cwd() / "outputs" / dir_nome
    output_dir.mkdir(parents=True, exist_ok=True)

    return output_dir

def next_available_file(directory: Path, stem="conversion", suffix=".wav"):
    i = 1
    while True:
        candidate = directory / f"{stem}_{i:03d}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1

def conversion(source, target, nome):
    out_dir = dir_diario(nome)
    out_file = next_available_file(out_dir)

    tts = TTS(
        model_name="voice_conversion_models/multilingual/multi-dataset/openvoice_v1",
        progress_bar=True
    )

    tts.voice_conversion_to_file(
        source_wav=str(source),
        target_wav=str(target),
        file_path=str(out_file)
    )

    print(f"Saved to: {out_file}")
    return str(out_file)

def gerar(referencia, prompt, i):
    clone = "tts_models/multilingual/multi-dataset/your_tts"
    print("Loading model...")
    tts = TTS(clone, gpu=False)
    print("Model loaded")

    nome_dir = f'{dir_diario()}'

    for i in range(i):
        print('Iteration', i + 1)
        now = str(datetime.datetime.now())
        file_name = now[11:19]
        file_path = unique_path(f'{nome_dir}/{file_name}.wav')

        tts.tts_to_file(
            text=str(prompt),
            speaker_wav=str(referencia),
            language='pt-br',
            file_path=f'outputs/{file_path}',
        )
        print(f"Saved output to outputs/{file_path} from reference file wav/{referencia}")

        referencia = file_path