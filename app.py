from flask import Flask, render_template, request
from model import get_product_image
from model import recommend_products
import pandas as pd

app = Flask(__name__)

# Load products for homepage cards
df = pd.read_csv("dataset.csv")


@app.route("/")
def home():
    featured = df.sample(12).copy()

    featured["image"] = featured.apply(
        lambda row: get_product_image(row["category"], row["product_name"]),
        axis=1
    )

    products = df["product_name"].tolist()

    return render_template(
        "index.html",
        featured=featured.to_dict(orient="records"),
        products=products
    )

@app.route("/recommend", methods=["POST"])
def recommend():
    product_name = request.form.get("product_name")
    results = recommend_products(product_name)

    return render_template(
        "results.html",
        product_name=product_name,
        results=results
    )


if __name__ == "__main__":
    app.run(debug=True)