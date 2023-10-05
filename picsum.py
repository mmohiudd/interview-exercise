import climage
from PIL import Image
import requests
from io import BytesIO
from base64 import b64encode

API_URL = 'https://picsum.photos/512/384'

def get_api_url(grayscale):
    """Return the API URL."""
    api_url = API_URL
    
    if grayscale is True:
        api_url += f"?grayscale"

    return api_url

def get_picture(grayscale=False, cli=False):
    """Get a picture from the picsum API - 5s the URL by default."""
    api_url = get_api_url(grayscale)
    image_data = None

    try:
        """Return the image from the API call."""
        response = requests.get(api_url)
        
        if cli is False:
            image_data = 'data:image/png;base64,' + b64encode(response.content).decode('ascii')
        else:
            image_data = climage.convert_pil(
                Image.open(BytesIO(response.content)).convert('RGB').resize((512, 384)), 
                is_unicode=True,                 
            )

            return image_data
    except:
        image_data = None
        
    return image_data