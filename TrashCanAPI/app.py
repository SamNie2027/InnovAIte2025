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
