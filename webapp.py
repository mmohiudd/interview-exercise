from flask import Flask, render_template, request
import random
import picsum
import forismatic

webapp = Flask(__name__, template_folder='templates')

@webapp.route('/', methods=['POST', 'GET'])
def index():
    key = int(request.form.get('key', 1))

    if(key not in range(1, 999999)):
        key = random.randint(1, 999999)

    quote = forismatic.get_quote()
    
    grayscale = bool(request.form.get('grayscale', 0))
    print(grayscale)
    image_data = picsum.get_picture(grayscale=grayscale)

    return render_template(
        "index.html", 
        image_data=image_data, quote=quote, key=key, grayscale=int(grayscale))

if __name__ == "__main__":
    webapp.run(debug=True)