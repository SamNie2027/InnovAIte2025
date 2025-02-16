from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/submitImage', methods=['POST'])
def submit_image():
    image = request.form['image']
    latitude = request.form['latitude']
    longitude = request.form['longitude']

    return 'received data'

if __name__ == '__main__':
    app.run(debug=True)
