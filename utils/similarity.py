from sklearn.metrics.pairwise import cosine_similarity


def find_similar_images(input_features, features, top_n=10):
    """Find the most similar images based on extracted features."""
    similarities = []
    for img_url, feature in features.items():
        similarity = cosine_similarity([input_features], [feature])
        similarities.append((img_url, similarity))

    # Sort by similarity and return the top N results
    similarities = sorted(similarities, key=lambda x: x[1], reverse=True)
    return [img[0] for img in similarities[:top_n]]
