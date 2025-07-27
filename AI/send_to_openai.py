
# TODO: Import your libaries
import base64
from openai import OpenAI
# TODO: Maybe you need a key?
from myAPI_KEY import API_KEY


client = OpenAI(api_key=API_KEY)

# Image encoding, code provided
def encode_image(image_path):
    with open(image_path, "rb") as image_F:
        return base64.b64encode(image_F.read()).decode('utf-8')


# TODO: Sending a request and getting a response
def getResponse(image_path):
    base64_image = encode_image(image_path)
    response = client.responses.create(
    model="gpt-4.1",
    input=[
        {
            "role": "user",
            "content": [
                { "type": "input_text", "text": "what's in this image?" },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    )
    print(response.output_text)
    return response.output_text




# TODO: How do we make things audible?
    


# TODO: Can we put everything together?

