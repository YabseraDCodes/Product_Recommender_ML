import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
df = pd.read_csv("dataset.csv")

# Combine important text columns
df["combined_text"] = (
    df["product_name"] + " " +
    df["category"] + " " +
    df["description"]
)

# Convert text into numeric vectors
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined_text"])

# Compare all products
similarity_matrix = cosine_similarity(tfidf_matrix)


def recommend_products(product_name, top_n=5):

    match = df[df["product_name"].str.lower() == product_name.lower()]

    if match.empty:
        return None

    product_index = match.index[0]

    scores = list(enumerate(similarity_matrix[product_index]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)
    scores = scores[1:top_n+1]

    results = []

    for i, score in scores:
        product = df.iloc[i]

        # 🔥 Extract "reason words"
        base_text = set(df.iloc[product_index]["combined_text"].lower().split())
        target_text = set(product["combined_text"].lower().split())

        common_words = list(base_text.intersection(target_text))

        # clean short/noisy words
        filtered_words = [w for w in common_words if len(w) > 3][:5]

        reason = ", ".join(filtered_words) if filtered_words else "similar category and features"

        results.append({
            "name": product["product_name"],
            "category": product["category"],
            "price": product["price"],
            "score": round(float(score), 3),
            "reason": reason,
            "image": get_product_image(product["category"], product["product_name"])
        })

    return results

def get_product_image(category, name):

    category = category.lower()
    name = name.lower()

    if "mouse" in name:
        return "https://images.unsplash.com/photo-1527814050087-3793815479db"
    if "keyboard" in name:
        return "https://images.unsplash.com/photo-1511467687858-23d96c32e4ae"
    if "monitor" in name:
        return "https://images.unsplash.com/photo-1587202372775-e229f172b9d7"
    if "headphone" in name or "earbuds" in name:
        return "https://images.unsplash.com/photo-1505740420928-5e560c06d30e"
    if "ssd" in name or "hdd" in name:
        return "https://images.unsplash.com/photo-1587829741301-dc798b83add3"
    if "router" in name:
        return "https://images.unsplash.com/photo-1606904825846-647eb07f5be2"
    if "laptop" in name:
        return "https://images.unsplash.com/photo-1517336714731-489689fd1ca8"
    if "usb" in name:
        return "https://images.unsplash.com/photo-1518770660439-4636190af475"

    # default fallback image
    return "https://images.unsplash.com/photo-1518770660439-4636190af475"
