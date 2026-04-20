# Product Recommendation System (Flask + ML)

## Project Overview

This is a full-stack AI-powered product recommendation system built
using Python, Flask, and Scikit-learn. It uses a content-based filtering
approach with TF-IDF vectorization and cosine similarity to recommend
similar products based on product descriptions.

------------------------------------------------------------------------

## Features

-   Content-based recommendation system
-   TF-IDF vectorization for text processing
-   Cosine similarity for product matching
-   Explainable recommendations (why a product is suggested)
-   Bootstrap-based  ecommerce UI
-   Dynamic featured products
-   Autocomplete search suggestions
-   Product images for better UI experience
-   Flask backend with routing

------------------------------------------------------------------------

## Project Structure

product-recommender/ │── app.py │── model.py │── dataset.csv │──
requirements.txt │── runtime.txt │── Procfile │── README.md │──
templates/ │ ├── index.html │ └── results.html │── static/ │ └──
style.css

------------------------------------------------------------------------

## Dataset

The dataset contains product information with:

-   product_name
-   category
-   description
-   price

------------------------------------------------------------------------

## Machine Learning Approach

### 1. Text Processing

Product name, category, and description are combined into one text
field.

### 2. TF-IDF Vectorization

Text is converted into numerical vectors using TF-IDF.

### 3. Cosine Similarity

Similarity between products is calculated using cosine similarity.

### 4. Recommendation Function

Returns top N most similar products.

------------------------------------------------------------------------

## How to Run Locally

### Clone repository

git clone https://github.com/YabseraDCodes/product-recommender.git cd
product-recommender

### Create virtual environment

python -m venv venv source venv/bin/activate

### Install dependencies

pip install -r requirements.txt

### Run app

python app.py

Open: http://127.0.0.1:5000


------------------------------------------------------------------------

## Key Concepts

-   TF-IDF Vectorization
-   Cosine Similarity
-   Content-based Filtering
-   Flask Web Development
-   Full-stack ML Deployment

------------------------------------------------------------------------

## Future Improvements

-   Collaborative filtering
-   Database integration
-   Authentication system
-   Improved ranking
