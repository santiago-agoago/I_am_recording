from pathlib import Path
from functions import *
from modelos import *


model = "freevc24"
print(f"\nTrying model: {model}")
#threading.Thread(target=stop_command, daemon=True).start()

file = 'wav/cumbia.wav'
for i in range(100):
    new_file = conversion_models(file, file, model, play=True)
    file = new_file

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