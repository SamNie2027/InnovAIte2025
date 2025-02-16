from flask import Flask, request
import os
app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))
print(f"Starting Flask app on port {port}...")  # EARLY PRINT

@app.route('/submitImage', methods=['POST'])
def submit_image():
    print('post called')
    raw_image = request.json['image']
    latitude = request.json['latitude']
    longitude = request.json['longitude']
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
    port = os.environ.get("PORT")
    print(f"PORT from environment: {port}")  # Debugging line

    if not port:
        print("⚠️ PORT environment variable is missing! Using default 5000.")
        port = 5000
    else:
        port = int(port)

    print(f"Running on port {port}")  # Debugging output
    app.run(debug=False, host='0.0.0.0', port=port)

