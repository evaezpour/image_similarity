from flask import Flask, request, json
import os
from utils.similarity import find_similar_images
from utils.storage import load_data
from config import FEATURES_FILE, MAP_FILE, UPLOAD_FOLDER

app = Flask(__name__)

# Load the features from the pickle file
features = load_data(FEATURES_FILE)
image_name_to_url = load_data(MAP_FILE)


# Define the POST endpoint
@app.route('/find_similar_images', methods=['POST'])
def find_similar_images_endpoint():
    # Get the uploaded image
    file = request.files['image']
    img_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(img_path)

    # Map the img_name to the img_url
    img_url = image_name_to_url.get(file.filename)
    if img_url is None:
        return "Image not found in dataset", 404

    # Extract features from the uploaded image
    input_features = features[img_url]
    if input_features is None:
        return "Features not found for the image URL", 404

    # Find similar images
    similar_images = find_similar_images(input_features, features)

    response = app.response_class(
        response=json.dumps(similar_images, ensure_ascii=False, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
