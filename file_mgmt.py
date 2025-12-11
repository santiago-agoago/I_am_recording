import os
import datetime
from uniqpath import unique_path
from TTS.api import TTS

def dir_diario():
    dia = str(datetime.datetime.now())
    dir_nome = dia[0:10]
    if os.path.isdir(dir_nome):
        print('Diretório já existe')
    else:
        os.makedirs(dir_nome, exist_ok=True)

    return dir_nome

def dir_especial(nome):
    dia = str(datetime.datetime.now())
    dir_nome = f'{str(nome)} {dia[0:10]}'
    if os.path.isdir(dir_nome):
        print('Diretório já existe')
    else:
        os.makedirs(dir_nome, exist_ok=True)

    return dir_nome

def feedback(referencia, prompt, i):
    clone = "tts_models/multilingual/multi-dataset/your_tts"
    print("Loading model...")
    tts = TTS(clone, gpu=False)
    print("Model loaded")

    nome_dir = f'{dir_especial("feedback")}'

    for i in range(i):
        print('Iteration', i + 1)
        now = str(datetime.datetime.now())
        file_name = now[11:19]
        file_path = unique_path(f'{nome_dir}/{file_name}.wav')

        tts.tts_to_file(
            text=str(prompt),
            speaker_wav=str(referencia),
            language='pt-br',
            file_path=file_path,
        )
        print(f"Saved output to {file_path} from reference file {referencia}")

        referencia = file_path