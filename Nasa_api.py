from flask import Flask, render_template, request
import urllib.request
import json



app = Flask(__name__)


@app.route("/home", methods=['POST'])
def home():
	apodurl = 'https://api.nasa.gov/planetary/apod?api_key='
        mykey = 'api_key=fOrNYkZMYt8KEwieCkuEcYJi3uMYQvQpvDDFjEmv'

	apodurlobj = urllib.request.urlopen(apodurl + mykey)

	apodread = apodurlobj.read()

	decodeapod = json.loads(apodread.decode('utf-8'))

	image= decodeapod['apodurl']

	return render_template('layout.html', picture=image)


if __name__ == '__main__':
    app.run(debug=True)


  


