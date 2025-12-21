from functions import *
from modelos import *

for model in VOICE_CONVERSION_MODELS:
    print(f"\nTrying model: {model}")

    file = 'wav/senoide.wav'
    for i in range(100):
        new_file = conversion_models(file, file, model, play=False)
        file = new_file

    file = 'wav/police_anthonyc.wav'
    for i in range(100):
        new_file = conversion_models(file, file, model, play=False)
        file = new_file