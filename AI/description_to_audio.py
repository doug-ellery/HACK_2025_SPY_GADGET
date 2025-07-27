import openai
from myAPI_KEY import API_KEY


def text_to_audio(words):
    openai.api_key = API_KEY

    response = openai.audio.speech.create(
    model="tts-1",               # Or use "tts-1-hd" for higher quality
    voice="alloy",               # Voices: alloy, echo, fable, onyx, nova, shimmer
    input=words,
    response_format="wav"        # Choose wav format
    )
    with open("../frontend/public/description.wav", "wb") as f:
        f.write(response.content)
    print("picture description written to description.wav")
    