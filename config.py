import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploaded_images')
FEATURES_FILE = os.path.join(BASE_DIR, 'image_features/features.pkl')
MAP_FILE = os.path.join(BASE_DIR, 'image_features/name_to_url_map.pkl')
DOWNLOAD_FOLDER = os.path.join(BASE_DIR, 'raw_images')
