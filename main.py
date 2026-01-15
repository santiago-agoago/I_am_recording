from pathlib import Path
from functions import *
from modelos import *

TEXT_PROMPT = "This is not a test"
REFERENCE_WAV = "wav/bittown_1/Untitled.wav"

# create dated output directory
OUT_DIR = dir_diario("tts_models")

results = {}

for short_name, model_name in TTS_MODELS.items():
    print(f"\n=== Testing model: {short_name} ===")
    try:
        tts = TTS(model_name=model_name, progress_bar=True)

        out_file = OUT_DIR / f"{short_name}.wav"

        tts.tts_to_file(
            text=str(TEXT_PROMPT),
            speaker_wav=str(REFERENCE_WAV),
            file_path=str(out_file),
        )

        play_wav(out_file, wait=False)

        results[short_name] = f"OK"
        print(f"✓ Saved → {out_file}")

    except Exception as e:
        results[short_name] = "FAILED"
        print(f"✗ Failed: {short_name}")
        print(e)

# ---------------- SUMMARY ----------------

print("\n===== SUMMARY =====")
for model, status in results.items():
    print(f"{model:25s} : {status}")
'''
model = "openvoice_v2"
print(f"\nTrying model: {model}")
#threading.Thread(target=stop_command, daemon=True).start()

file = 'wav/senoide.wav'
for i in range(1):
    new_file = conversion_models(file, file, model, play=True)
    file = new_file

file = 'wav/police_anthonyc.wav'
for i in range(100):
    new_file = conversion_models(file, file, model, play=True)
    file = new_file
'''

'''
file = Path('wav/bittown_1/Untitled4.wav')

for model in VOICE_CONVERSION_MODELS:
    print(f"\nTrying model: {model}")
    conversion_models(file, file, model, play=True)

#for file in folder.iterdir():

TEXT_PROMPT = "This is a test sentence to evaluate the voice quality."
REFERENCE_WAV = "reference.wav"

# create dated output directory
OUT_DIR = dir_diario("tts_models")
'''