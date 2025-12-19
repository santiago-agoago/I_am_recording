# DICIONÁRIO COM TODOS OS MODELOS

TTS_MODELS = {
    "xtts_v2": "tts_models/multilingual/multi-dataset/xtts_v2",
    "xtts_v1_1": "tts_models/multilingual/multi-dataset/xtts_v1.1",
    "your_tts": "tts_models/multilingual/multi-dataset/your_tts",
    "bark": "tts_models/multilingual/multi-dataset/bark",

    "vits_bg": "tts_models/bg/cv/vits",
    "vits_cs": "tts_models/cs/cv/vits",
    "vits_da": "tts_models/da/cv/vits",
    "vits_et": "tts_models/et/cv/vits",
    "vits_ga": "tts_models/ga/cv/vits",

    "tacotron2_ek1": "tts_models/en/ek1/tacotron2",

    "tacotron2_ljs_ddc": "tts_models/en/ljspeech/tacotron2-DDC",
    "tacotron2_ljs_ddc_ph": "tts_models/en/ljspeech/tacotron2-DDC_ph",
    "glow_tts_ljs": "tts_models/en/ljspeech/glow-tts",
    "speedy_speech": "tts_models/en/ljspeech/speedy-speech",
    "tacotron2_ljs_dca": "tts_models/en/ljspeech/tacotron2-DCA",
    "vits_ljs": "tts_models/en/ljspeech/vits",
    "vits_ljs_neon": "tts_models/en/ljspeech/vits--neon",
    "fast_pitch_ljs": "tts_models/en/ljspeech/fast_pitch",
    "overflow_ljs": "tts_models/en/ljspeech/overflow",
    "neural_hmm_ljs": "tts_models/en/ljspeech/neural_hmm",

    "vits_vctk": "tts_models/en/vctk/vits",
    "fast_pitch_vctk": "tts_models/en/vctk/fast_pitch",
    "tacotron_ddc_sam": "tts_models/en/sam/tacotron-DDC",

    "capacitron_c50": "tts_models/en/blizzard2013/capacitron-t2-c50",
    "capacitron_c150": "tts_models/en/blizzard2013/capacitron-t2-c150_v2",

    "tortoise_v2": "tts_models/en/multi-dataset/tortoise-v2",
    "jenny": "tts_models/en/jenny/jenny",

    "tacotron2_es": "tts_models/es/mai/tacotron2-DDC",
    "vits_es": "tts_models/es/css10/vits",

    "tacotron2_fr": "tts_models/fr/mai/tacotron2-DDC",
    "vits_fr": "tts_models/fr/css10/vits",

    "glow_tts_uk": "tts_models/uk/mai/glow-tts",
    "vits_uk": "tts_models/uk/mai/vits",

    "tacotron2_zh": "tts_models/zh-CN/baker/tacotron2-DDC-GST",

    "tacotron2_nl": "tts_models/nl/mai/tacotron2-DDC",
    "vits_nl": "tts_models/nl/css10/vits",

    "tacotron2_de_dca": "tts_models/de/thorsten/tacotron2-DCA",
    "vits_de": "tts_models/de/thorsten/vits",
    "tacotron2_de_ddc": "tts_models/de/thorsten/tacotron2-DDC",
    "vits_de_neon": "tts_models/de/css10/vits-neon",

    "tacotron2_ja": "tts_models/ja/kokoro/tacotron2-DDC",

    "glow_tts_tr": "tts_models/tr/common-voice/glow-tts",

    "glow_tts_it_f": "tts_models/it/mai_female/glow-tts",
    "vits_it_f": "tts_models/it/mai_female/vits",
    "glow_tts_it_m": "tts_models/it/mai_male/glow-tts",
    "vits_it_m": "tts_models/it/mai_male/vits",

    "vits_ewe": "tts_models/ewe/openbible/vits",
    "vits_hau": "tts_models/hau/openbible/vits",
    "vits_lin": "tts_models/lin/openbible/vits",
    "vits_tw_aku": "tts_models/tw_akuapem/openbible/vits",
    "vits_tw_asa": "tts_models/tw_asante/openbible/vits",
    "vits_yor": "tts_models/yor/openbible/vits",

    "vits_hu": "tts_models/hu/css10/vits",
    "vits_el": "tts_models/el/cv/vits",
    "vits_fi": "tts_models/fi/css10/vits",
    "vits_hr": "tts_models/hr/cv/vits",
    "vits_lt": "tts_models/lt/cv/vits",
    "vits_lv": "tts_models/lv/cv/vits",
    "vits_mt": "tts_models/mt/cv/vits",
    "vits_pl": "tts_models/pl/mai_female/vits",
    "vits_pt": "tts_models/pt/cv/vits",
    "vits_ro": "tts_models/ro/cv/vits",
    "vits_sk": "tts_models/sk/cv/vits",
    "vits_sl": "tts_models/sl/cv/vits",
    "vits_sv": "tts_models/sv/cv/vits",

    "vits_ca": "tts_models/ca/custom/vits",
    "glow_tts_fa": "tts_models/fa/custom/glow-tts",
    "vits_bn_m": "tts_models/bn/custom/vits-male",
    "vits_bn_f": "tts_models/bn/custom/vits-female",
    "glow_tts_be": "tts_models/be/common-voice/glow-tts",
}

VOCODER_MODELS = {
    "wavegrad_uni": "vocoder_models/universal/libri-tts/wavegrad",
    "melgan_uni": "vocoder_models/universal/libri-tts/fullband-melgan",

    "wavegrad_ek1": "vocoder_models/en/ek1/wavegrad",
    "wavlm_hifigan": "vocoder_models/en/librispeech100/wavlm-hifigan",
    "wavlm_hifigan_pm": "vocoder_models/en/librispeech100/wavlm-hifigan_prematched",

    "melgan_ljs": "vocoder_models/en/ljspeech/multiband-melgan",
    "hifigan_ljs_v2": "vocoder_models/en/ljspeech/hifigan_v2",
    "univnet_ljs": "vocoder_models/en/ljspeech/univnet",

    "hifigan_blizz": "vocoder_models/en/blizzard2013/hifigan_v2",
    "hifigan_vctk": "vocoder_models/en/vctk/hifigan_v2",
    "hifigan_sam": "vocoder_models/en/sam/hifigan_v2",

    "pwg_nl": "vocoder_models/nl/mai/parallel-wavegan",

    "wavegrad_de": "vocoder_models/de/thorsten/wavegrad",
    "melgan_de": "vocoder_models/de/thorsten/fullband-melgan",
    "hifigan_de_v1": "vocoder_models/de/thorsten/hifigan_v1",

    "hifigan_ja": "vocoder_models/ja/kokoro/hifigan_v1",
    "melgan_uk": "vocoder_models/uk/mai/multiband-melgan",
    "hifigan_tr": "vocoder_models/tr/common-voice/hifigan",
    "hifigan_be": "vocoder_models/be/common-voice/hifigan",
}

VOICE_CONVERSION_MODELS = {
    "freevc24": "voice_conversion_models/multilingual/vctk/freevc24",
    "knnvc": "voice_conversion_models/multilingual/multi-dataset/knnvc",
    "openvoice_v1": "voice_conversion_models/multilingual/multi-dataset/openvoice_v1",
    "openvoice_v2": "voice_conversion_models/multilingual/multi-dataset/openvoice_v2",
}
