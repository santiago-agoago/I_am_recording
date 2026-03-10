import datetime
import simpleaudio as sa
import traceback
import threading
from TTS.api import TTS
from pathlib import Path
from modelos import *


# cria um diretório em outputs/ com um prefixo e o dia que foi gerado
def dir_diario(tipo):
    now = datetime.datetime.now().strftime("%Y-%m-%d")
    dir_nome = f"{tipo}.{now}"

    output_dir = Path.cwd() / "outputs" / dir_nome
    output_dir.mkdir(parents=True, exist_ok=True)

    return output_dir

# cria um arquivo com nome único e sufixo 001, 002 ... 00N
def next_available_file(directory: Path, model, suffix=".wav"):
    i = 1
    while True:
        candidate = directory / f"{model}_{i:03d}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1

# openvoice_v1 modelo de conversão
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

# itera sobre todos os modelos de conversão
def conversion_models(source, target, model, play=True):

    # try / except para que código não seja interrompido por erro em um dos modelos
    try:
        out_dir = dir_diario(model)
        out_file = next_available_file(out_dir, model)

        tts = TTS(
            model_name=str(VOICE_CONVERSION_MODELS[model]),
            progress_bar=True
        )

        tts.voice_conversion_to_file(
            source_wav=str(source),
            target_wav=str(target),
            file_path=str(out_file)
        )

        # cria ou modifica metadata.txt
        write_metadata(
            out_dir=out_dir,
            model=model,
            source=source,
            target=target,
            prompt=prompt,
            extra={
                "output_file": out_file
            }
        )

        print(f"[OK] {model} → Saved to: {out_file}")

        if play:
            print("PLAYING ...")
            play_wav(out_file, wait=False)

        return str(out_file)

    except Exception as e:
        print(f"[SKIP] {model} failed: {e}")
        return None

# foi o chatgpt .....
def write_metadata(
    out_dir,
    model,
    source,
    target,
    prompt,
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
        f.write(f"prompt: {prompt}\n")

        if extra:
            for key, value in extra.items():
                f.write(f"{key}: {value}\n")

        f.write("\n")

# reproduzir .wav assim que é gerado
def play_wav(path, wait=True):
    """
    Plays a WAV file.
    If wait=True, blocks until playback finishes.
    """
    global current_playback

    wave_obj = sa.WaveObject.from_wave_file(str(path))
    current_playback = wave_obj.play()

    if wait:
        current_playback.wait_done()

def synthesize_with_fallback(tts, text, out_path, reference_wav, play=True):
    """
    Try speaker_wav first, fallback to plain TTS if not supported.
    """
    try:
        # attempt voice cloning
        tts.tts_to_file(
            text=text,
            speaker_wav=reference_wav,
            file_path=out_path
        )
        if play:
            print("PLAYING ...")
            play_wav(out_file, wait=False)

        return str(out_file)

    except Exception:
        # fallback: plain synthesis
        tts.tts_to_file(
            text=text,
            file_path=out_path
        )
        return "no_speaker"

def tts_models(source, prompt, model, play=True):

    try:
        out_dir = dir_diario(model)
        out_file = next_available_file(out_dir, model)

        tts = TTS(
            model_name=str(TTS_MODELS[model]),
            progress_bar=True
        )

        # possible argument combinations
        attempts = [
            {"speaker_wav": source, "language": "en"},
            {"speaker_wav": source},
            {"language": "en"},
            {}
        ]

        success_args = None

        for args in attempts:
            try:
                clean_args = {k: str(v) for k, v in args.items() if v is not None}

                tts.tts_to_file(
                    text=str(prompt),
                    file_path=str(out_file),
                    **clean_args
                )

                success_args = clean_args
                break

            except Exception:
                continue

        if success_args is None:
            raise RuntimeError("All synthesis attempts failed")

        # create or update metadata
        write_metadata(
            out_dir=out_dir,
            model=model,
            source=source,
            target=prompt,
            prompt=prompt,
            extra={
                "output_file": str(out_file),
                "model_path": TTS_MODELS[model],
                "arguments_used": success_args
            }
        )

        print(f"[OK] {model} → Saved to: {out_file}")

        if play:
            print("PLAYING ...")
            play_wav(out_file, wait=False)

        return str(out_file)

    except Exception as e:
        print(f"[SKIP] {model} failed: {e}")
        return None

def run_all_models(source, prompt, play=True):

    results = {}

    for model in TTS_MODELS:

        print("\n==============================")
        print(f"Testing model: {model}")
        print("==============================")

        output = tts_models(
            source=source,
            prompt=prompt,
            model=model,
            play=play
        )

        results[model] = output

    return results