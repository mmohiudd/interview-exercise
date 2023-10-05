import random
import requests

API_URL = 'http://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en'


def get_api_url(key):
    """Return the API URL."""
    api_url = API_URL
    
    if key is None:
        key = random.randint(1, 999999)
    
    api_url += f"&key={key}"

    return api_url

def get_quote(key=None):
    """Get a quote from the forismatic API."""
    api_url = get_api_url(key)

    try:
        response = requests.get(api_url)
        
        return response.json().get(
            'quoteText', 
            None)
    except:
        return None

    
    
    