from pathlib import Path
from functions import *
from modelos import *

directory = Path('wav/drum_breaks/v3')

for file in sorted(directory.glob("*.wav")):
        print("\n====================================")
        print(f"Processing file: {file}")
        print("====================================")

        for model in VOICE_CONVERSION_MODELS:

            print(f"\nTrying model: {model}")

            for i in range(5):
                new_file = conversion_models(
                    source=file,
                    target=file,
                    model=model,
                    play=True
                )
                file = new_file

'''
#for file in folder.iterdir():

TEXT_PROMPT = "This is a test sentence to evaluate the voice quality."
REFERENCE_WAV = "reference.wav"

# create dated output directory
OUT_DIR = dir_diario("tts_models")
'''

'''
source = "DICOMDIR.wav"
prompt = "Hace once años, uno de los poetas insignes de nues-tro tiempo, el chileno Pablo Neruda, iluminó este ámbitocon su palabra"

run_all_models(source, prompt, play=True)
'''