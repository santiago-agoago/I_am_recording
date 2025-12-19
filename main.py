from TTS.api import TTS
#import sounddevice as sd
from file_mgmt import *
import os.path as os
from modelos import *

file = "outputs/saracura.2025-12-19/conversion_001.wav"

target = "wav/speech.wav"
source = target

for model in VOICE_CONVERSION_MODELS:
    print(f"\nTrying model: {model}")
    for i in range(10):
        new_file = conversion_models(file, file, model)
        file = new_file
