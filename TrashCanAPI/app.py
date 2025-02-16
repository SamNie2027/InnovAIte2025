from flask import Flask, jsonify, request
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
        
        if not data:
            return jsonify({"error": "Invalid request, no JSON received"}), 400

        raw_image = data.get('image')
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if not all([raw_image, latitude, longitude]):
            return jsonify({"error": "Missing required fields"}), 400

        print("Received image:", raw_image)
        print("Latitude:", latitude)
        print("Longitude:", longitude)

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
    app.run(debug=False, host='0.0.0.0', port=port)
