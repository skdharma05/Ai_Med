from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient()

def synthesize_speech(text, filename):
    output_path = f"audio/{filename}.mp3"
    synthesis_input = texttospeech.SynthesisInput(text=text)

    voice = texttospeech.VoiceSelectionParams(
        language_code="en-US",
        name="en-US-Wavenet-F",
        ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )

    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3,
        speaking_rate=0.95,
        pitch=2.0
    )

    response = client.synthesize_speech(
        input=synthesis_input, voice=voice, audio_config=audio_config
    )

    os.makedirs("audio", exist_ok=True)
    with open(output_path, "wb") as out:
        out.write(response.audio_content)
    return output_path
