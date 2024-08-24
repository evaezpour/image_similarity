from flask import Flask, request, json
import os
from utils.feature_extraction import extract_features
from utils.similarity import find_similar_images
from utils.storage import load_features
from config import UPLOAD_FOLDER

app = Flask(__name__)

# Load the features from the pickle file
features = load_features()


# Define the POST endpoint
@app.route('/find_similar_images', methods=['POST'])
def find_similar_images_endpoint():
    # Get the uploaded image
    file = request.files['image']
    img_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(img_path)

    # Extract features from the uploaded image
    input_features = extract_features(img_path)

    # Find similar images
    similar_images = find_similar_images(input_features, features)

    ## Return the URLs of similar images as JSON
    #return jsonify(similar_images)

    response = app.response_class(
        response=json.dumps(similar_images, ensure_ascii=False, indent=4),
        status=200,
        mimetype='application/json'
    )
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
