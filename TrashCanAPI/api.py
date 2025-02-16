from flask import Flask, request
from preprocess import *
import determineIfFull
import updateTrashCanStatus
import CompareImagesModel
import FullnessModel

app = Flask(__name__)

@app.route('/submitImage', methods=['POST'])
def submit_image(fullness_model, compare_model):
    raw_image = request.form['image']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    city_worker = request.form['city_worker'] # expected to be a boolean
    image = preprocess(raw_image)
    if (image):
        if (city_worker):
            full_likelihood = -1
        else:
            full_likelihood = determineIfFull(image, fullness_model)

        updateTrashCanStatus(image, latitude, longitude, full_likelihood, compare_model)
        
    

    return 'received data'

if __name__ == '__main__':
    app.run(debug=True)
    fullness_model = FullnessModel()
    compare_model = CompareImagesModel()
