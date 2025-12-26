from functions import *
from modelos import *

model = "openvoice_v2"
print(f"\nTrying model: {model}")
threading.Thread(target=stop_command, daemon=True).start()

file = 'wav/police_anthonyb.wav'
for i in range(100):
    new_file = conversion_models(file, file, model, play=True)
    file = new_file

file = 'wav/police_anthonyc.wav'
for i in range(100):
    new_file = conversion_models(file, file, model, play=True)
    file = new_file