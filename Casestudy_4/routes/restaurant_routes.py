
from flask import  request, jsonify, Blueprint

from data.datastore import restaurants, dishes, ratings

restaurant_bp=Blueprint('restaurant_bp',__name__)
@restaurant_bp.route('/api/v1/restaurants',methods=['POST'])
def add_restaurant():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Restaurant name is required"}), 400
    for restaurant in restaurants:
        if restaurant["name"] == data["name"]:
            return jsonify({"error": "Restaurant name already exists"}), 409
    restaurant={
        "id":len(restaurants)+1,
        "name":data["name"],
        "category":data.get("category"),
        "location":data.get("location"),
        "images":data.get("images"),
        "contact":data.get("contact"),
        "enabled":True,
        "approved":True,
    }
    restaurants.append(restaurant)
    return jsonify(restaurants),201
@restaurant_bp.route('/api/v1/restaurants/<int:rid>',methods=['GET'])
def get_restaurant(rid):
    for restaurant in restaurants:
        if restaurant["id"] == rid:
            return jsonify(restaurant),200
    return jsonify({"error": "Restaurant not found"}), 404
@restaurant_bp.route('/api/v1/restaurants/<int:rid>',methods=['PUT'])
def update_restaurant(rid):
    data = request.get_json()
    for restaurant in restaurants:
        if restaurant["id"] == rid:
            restaurant.update(data)
            return jsonify(restaurant),200
    return jsonify({"error": "Restaurant not found"}), 404
@restaurant_bp.route('/api/v1/restaurants/<int:rid>/disable',methods=['PUT'])
def disable_restaurant(rid):
    for restaurant in restaurants:
        if restaurant["id"] == rid:
            restaurant["enabled"] = False
            return jsonify({"message": "Restaurant disabled"})
    return jsonify({"error": "Restaurant not found"}), 404
@restaurant_bp.route('/api/v1/restaurants/search',methods=['GET'])
def search_restaurants():
    name = request.args.get("name")
    location = request.args.get("location")
    dish_name = request.args.get("dish")
    rating = request.args.get("rating")

    result = restaurants

    if name:
        result = [r for r in result if name.lower() in r["name"].lower()]

    if location:
        result = [r for r in result if location.lower() in r["location"].lower()]

    if dish_name:
        restaurant_ids = [
            d["restaurant_id"] for d in dishes
            if dish_name.lower() in d["name"].lower()
        ]
        result = [r for r in result if r["id"] in restaurant_ids]

    if rating:
        rating = float(rating)
        restaurant_ids = [
            rt["restaurant_id"] for rt in ratings
            if rt["rating"] >= rating
        ]
        result = [r for r in result if r["id"] in restaurant_ids]

    return jsonify(result), 200