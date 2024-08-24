# Image Similarity Web Service

## Overview

This project implements a web service that allows users to upload an image and returns a list of the most similar images from a predefined set. The service is built using Flask, and it leverages TensorFlow and scikit-learn for image feature extraction and similarity comparison.

## Features

- **Image Upload**: Users can upload an image via a POST request.
- **Image Similarity**: The service returns the top N most similar images based on precomputed features.
- **Lightweight Deployment**: The service is containerized using Docker for easy deployment. 
The raw images and their extracted features are placed outside of the docker image. 
- **Feature Extraction**: A pre-trained VGG network is used for feature extraction. 
VGG is a strong and reliable option for feature extraction in image similarity tasks.
- **Image Similarity metric**: Cosine similarity is used for similarity metric.

## Setup Instructions

### Prerequisites

- Python 3.9+
- Docker
- Pip

### Step 1: Clone the Repository

git clone https://github.com/evaezpour/image_similarity

cd image_similarity

### Step 2: Install Dependencies
If you plan to run the project locally (without Docker), install the necessary Python dependencies:

pip install -r requirements.txt

### Step 3: Prepare the Features
Download the raw images and precompute the features, and save them to a directory outside of the Docker image:

pip install tensorflow

Run the 'prepare_data.py' file.

### Step 4: Running the project locally

Run the 'app.py' file. Go to Step 7 to interact with the web service. 

### Step 5: Build the Docker Image

Build the Docker image, excluding unnecessary files:

docker build -t image_similarity_service .

### Step 6: Run the Docker Container

If the 'features.pkl' file is stored locally on your host machine, run the container with a mounted volume:

docker run -p 5000:5000 -v D:/image_features:/app/image_features image_similarity_service

### Step 7: Access the Web Service
Once the container is running, you can interact with the web service. The API provides an endpoint to upload images and retrieve similar images.

Example Usage with curl:

- open cmd

- curl -X POST -F "image=@/path/to/image.jpg" http://127.0.0.1:5000/find_similar_images

Example Response:

[

    "https://valentino-cdn.thron.com/delivery/public/thumbnail/valentino/d99d8f54-848f-4ba8-b9b2-d1d6a57edd94/ihqstx/std/500x0/-?quality=80&size=35&format=auto",

    "https://valentino-cdn.thron.com/delivery/public/thumbnail/valentino/db30c834-3938-4e8d-b421-ff85c3c700fa/ihqstx/std/500x0/CREPE-COUTURE-TROUSERS-?quality=80&size=35&format=auto",

    "https://valentino-cdn.thron.com/delivery/public/thumbnail/valentino/6a6ba1d3-9cab-4984-9495-d4b524bb71bd/ihqstx/std/500x0/COMPACT-POPELINE-SKIRT-?quality=80&size=35&format=auto",

...

]

