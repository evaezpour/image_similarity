import pickle
from config import FEATURES_FILE


def load_features(file_path=FEATURES_FILE):
    """Load the features from a pickle file."""
    with open(file_path, 'rb') as f:
        features = pickle.load(f)
    return features


def save_features(features, file_path=FEATURES_FILE):
    """Save the features to a pickle file."""
    with open(file_path, 'wb') as f:
        pickle.dump(features, f)
