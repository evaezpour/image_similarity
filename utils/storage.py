import pickle


def load_data(file_path):
    """Load the features from a pickle file."""
    with open(file_path, 'rb') as f:
        features = pickle.load(f)
    return features


def save_data(features, file_path):
    """Save the features to a pickle file."""
    with open(file_path, 'wb') as f:
        pickle.dump(features, f)
