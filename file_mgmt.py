import os
import datetime
from uniqpath import unique_path
from TTS.api import TTS
from pathlib import Path
from modelos import *


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

def conversion_models(source, target, model):
    try:
        out_dir = dir_diario(model)
        out_file = next_available_file(out_dir)

        tts = TTS(
            model_name=str(VOICE_CONVERSION_MODELS[model]),
            progress_bar=True
        )

        tts.voice_conversion_to_file(
            source_wav=str(source),
            target_wav=str(target),
            file_path=str(out_file)
        )

        write_metadata(
            out_dir=out_dir,
            model=model,
            source=source,
            target=target,
            extra={
                "output_file": out_file
            }
        )
        print(f"[OK] {model} → Saved to: {out_file}")
        return str(out_file)

    except Exception as e:
        print(f"[SKIP] {model} failed: {e}")
        return None

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

def write_metadata(
    out_dir,
    model,
    source,
    target,
    extra=None
):
    """
    Creates or appends a metadata.txt file inside out_dir
    """
    out_dir = Path(out_dir)
    metadata_file = out_dir / "metadata.txt"

    with metadata_file.open("a", encoding="utf-8") as f:
        f.write("====================================\n")
        f.write(f"timestamp: {datetime.datetime.now().isoformat()}\n")
        f.write(f"model: {model}\n")
        f.write(f"model_path: {VOICE_CONVERSION_MODELS.get(model)}\n")
        f.write(f"source: {source}\n")
        f.write(f"target: {target}\n")

        if extra:
            for key, value in extra.items():
                f.write(f"{key}: {value}\n")

        f.write("\n")