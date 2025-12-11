from TTS.api import TTS
import sounddevice as sd
from uniqpath import unique_path
from file_mgmt import *
import whisper

# outros modelos:
# modelo_pt = "tts_models/pt/cv/vits"
# modelo_es = "tts_models/es/mai/tacotron2-DDC"

referencia = "senoide.wav"

prompt = "Estou sentado em uma sala"

# feedback("16:33:08.wav","eu estava caminhandoando kkkkkkkkkk.......", 100)

model = whisper.load_model("turbo")
result = model.transcribe("speech.wav")
print(result["text"])