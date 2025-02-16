from flask import Flask, request
import os

app = Flask(__name__)

# Set the max content length for incoming requests (in bytes)
app.config['MAX_CONTENT_LENGTH'] = 100 * 1024 * 1024  # 100 MB limit

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