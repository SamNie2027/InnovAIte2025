from flask import Flask, request
from preprocess import preprocess
from updateTrashCanStatus import updateTrashCanStatus
from CompareImagesModel import CompareImagesModel
from FullnessModel import FullnessModel

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
            full_likelihood = fullness_model.predict(image)

        updateTrashCanStatus(image, latitude, longitude, full_likelihood, compare_model) # NOT IMPLEMENTED 

    return 'received data'

if __name__ == '__main__':
    app.run(debug=True)
    # initialize models
    fullness_model = FullnessModel()
    compare_model = CompareImagesModel()
