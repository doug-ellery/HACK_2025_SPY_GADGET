
# TODO: Import your libaries
from openai import OpenAI
# TODO: Maybe you need a key?
from myAPI_KEY import API_KEY


# Image encoding, code provided
def encode_image(image_path):
    with open(image_path, "rb") as image_F:
        return base64.b64encode(image_F.read()).decode('utf-8')


# TODO: Sending a request and getting a response



# TODO: How do we make things audible?
    


# TODO: Can we put everything together?

