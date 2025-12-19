from functions import *
from modelos import *

for model in VOICE_CONVERSION_MODELS:
    print(f"\nTrying model: {model}")

    source = "wav/DICOMDIR.wav"
    target = "wav/abril.wav"
    conversion_models(source, target, model)