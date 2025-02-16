from flask import Flask, request
import preprocess

app = Flask(__name__)

@app.route('/submitImage', methods=['POST'])
def submit_image():
    image = request.form['image']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    processed = preprocess(image)
    if (processed):
        sendModel1(processed, latitude, longitude)
        sendModel2(processed)
    

    return 'received data'

if __name__ == '__main__':
    app.run(debug=True)
