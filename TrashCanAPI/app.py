from flask import Flask, request
import os
app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))
print(f"Starting Flask app on port {port}...")  # EARLY PRINT

@app.route('/submitImage', methods=['POST'])
def submit_image(fullness_model, compare_model):
    raw_image = request.form['image']
    latitude = request.form['latitude']
    longitude = request.form['longitude']
    print(raw_image)
    print(latitude)
    print(longitude)
    # city_worker = request.form['city_worker'] # expected to be a boolean
    # image = preprocess(raw_image)
    # if (image):
    #     if (city_worker):
    #         full_likelihood = -1
    #     else:
    # full_likelihood = fullness_model.predict(image)
    # 
    # updateTrashCanStatus(image, latitude, longitude, 1, compare_model) # NOT IMPLEMENTED 

    return 'received data'

if __name__ == '__main__':
    print(f"Running on port {port}")  # PRINT FOR DEBUG
    app.run(debug=True, host='0.0.0.0', port=port)
    # initialize models
    # fullness_model = FullnessModel()
    # compare_model = CompareImagesModel()
