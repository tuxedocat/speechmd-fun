from google.cloud import texttospeech as tts
import sys
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(f"{sys.argv[0]}")

c = tts.TextToSpeechClient()

try:
    fn = sys.argv[1]
    with open(fn, "r") as f:
        s = f.read()
except IndexError:
    s = sys.stdin.read()


tts_input = tts.SynthesisInput(ssml=s)
voice = tts.VoiceSelectionParams(
    language_code="ja-JP", 
    name="ja-JP-Wavenet-D",
    # name="ja-JP-Standard-D",
    ssml_gender=tts.SsmlVoiceGender.MALE
)

audio_config = tts.AudioConfig(audio_encoding=tts.AudioEncoding.MP3)
response = c.synthesize_speech(input=tts_input, voice=voice, audio_config=audio_config)

try:
    outfn = sys.argv[2]
except IndexError:
    outfn = "output.mp3"

with open(outfn, "wb") as out:
    out.write(response.audio_content)
