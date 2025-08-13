from flask import Flask, jsonify, request
from data import products

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Product API"}), 200

@app.route("/products", methods=["GET"])
def get_products():
    category = request.args.get("category")
    if category:
        wanted = category.strip().lower()
        filtered = [p for p in products if p.get("category", "").lower() == wanted]
        return jsonify(filtered), 200
    return jsonify(products), 200

@app.route("/products/<int:id>", methods=["GET"])
def get_product_by_id(id):
    for p in products:
        if p.get("id") == id:
            return jsonify(p), 200
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)