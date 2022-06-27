from base64 import b64encode
from requests import post

class ocr:
    def __init__(self, api_key: str, image):
        self.api_key = api_key
        self.image = open(image, 'rb').read()
        self.b64_image = b64encode(self.image).decode()

    def get_text(self):
        payload = {
            'apikey': self.api_key,
            'base64image': f'data:image/jpg;base64,{self.b64_image}'
        }
        resp = post('https://api.ocr.space/parse/image', data=payload).json()
        return resp['ParsedResults'][0]['ParsedText']