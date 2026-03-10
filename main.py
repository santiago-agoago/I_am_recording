from pathlib import Path
from functions import *
from modelos import *

source = "DICOMDIR.wav"
prompt = "Hace once años, uno de los poetas insignes de nues-tro tiempo, el chileno Pablo Neruda, iluminó este ámbitocon su palabra"

run_all_models(source, prompt, play=True)

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