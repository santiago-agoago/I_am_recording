import sounddevice as sd

# Seria melhor reproduzir o arquivo assim que ele é criado

speaker = tts.speakers[0]
language = "pt"

audio = tts.tts(
    text=prompt,
    speaker_wav=referencia,
    language='pt-br'
)

sd.play(audio, samplerate=22050)
sd.wait()