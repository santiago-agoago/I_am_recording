from TTS.api import TTS
#import sounddevice as sd
from file_mgmt import *
import os.path as os

file = "wav/sem_moralismo.wav"

for i in range(1):
    new_file = conversion(file, file, "sem_moralismo")
    file = new_file
    print("iteração ", i)