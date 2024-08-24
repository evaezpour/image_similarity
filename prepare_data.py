import pandas as pd
import requests
import os
from utils.feature_extraction import extract_features
from utils.storage import save_features
from config import DOWNLOAD_FOLDER, FEATURES_FILE

# Define the URL of your CSV file
csv_url = 'https://xgen-interview-dataset.s3.amazonaws.com/valentino_links.csv'

# Load the CSV file
df = pd.read_csv(csv_url, header=None, skiprows=1, names=["image_url"])

# Create a directory to store the images if it doesn't exist
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)


# Function to sanitize filenames
def sanitize_filename(filename):
    return filename.replace("\n", "").replace("\r", "").replace("/", "_").replace("\\", "_").replace(",", "")


# Download images and extract features
features = {}
failed_download = 0
for index, row in df.iterrows():
    print(index)
    img_url = row['image_url'].strip()
    img_name = sanitize_filename(img_url.split("/")[-1].split("?")[0])  # Extract a clean image name
    img_name += f'_{index}'
    img_path = os.path.join(DOWNLOAD_FOLDER, f"{img_name}.jpg")

    try:
        # Download the image
        response = requests.get(img_url)
        response.raise_for_status()  # Ensure the request was successful
        with open(img_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {img_name}.jpg successfully.")

        # Extract and save features
        features[img_url] = extract_features(img_path)

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {img_url}: {e}")
        failed_download += 1
    except Exception as e:
        print(f"Error processing {img_name}.jpg: {e}")
        failed_download += 1

print(f"failed to download {failed_download} number of images")
# Save the features to a file
save_features(features, FEATURES_FILE)
print(f"Features have been saved to {FEATURES_FILE}.")
