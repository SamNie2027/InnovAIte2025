from flask import Flask, jsonify, request
from preprocess import preprocess
# from updateTrashCanStatus import updateTrashCanStatusMain
# from CompareImagesModel import CompareImagesModel
# from CompareImagesTFModel import CompareImagesModel
# from FullnessModel import FullnessModel
import os

app = Flask(__name__)

# Set the max content length for incoming requests (in bytes)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit

port = int(os.environ.get("PORT", 5000))
print(f"Starting Flask app on port {port}...")  # EARLY PRINT

@app.route('/submitImage', methods=['POST'])
def submit_image():
    try:
        data = request.get_json()
        
        print("Received JSON:", data)  # Debugging output

        if not data:
            return jsonify({"error": "Invalid request, no JSON received"}), 400

        required_fields = ["image", "latitude", "longitude"]
        missing_fields = [field for field in required_fields if field not in data]

        if missing_fields:
            return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

        raw_image = data["image"]
        latitude = data["latitude"]
        longitude = data["longitude"]

        # city_worker = request.form['city_worker'] # expected to be a boolean
        image = preprocess(raw_image)
        # if (image):
        #     if (city_worker):
        #         full_likelihood = -1
        #     else:
        #         full_likelihood = fullness_model.predict(image)
        # 
        full_likelihood = 1
        # updateTrashCanStatusMain(image, latitude, longitude, full_likelihood, compare_model) # NOT IMPLEMENTED 

        response = {
            "message": "Image received successfully",
            "data": {
                "latitude": latitude,
                "longitude": longitude
            }
        }
        return jsonify(response), 200  # HTTP 200 OK

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # Internal Server Error

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
    # initialize models
    # fullness_model = FullnessModel()
    # compare_model = CompareImagesModel()
