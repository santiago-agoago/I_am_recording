import sounddevice as sd


# Choose one speaker and language
speaker = tts.speakers[0]
language = "pt"

#play
audio = tts.tts(
    text=prompt,
    speaker_wav=referencia,
    language='pt-br'
)

sd.play(audio, samplerate=22050)
sd.wait()