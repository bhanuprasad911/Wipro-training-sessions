from flask import Flask, jsonify, request, Blueprint

from data.datastore import dishes

dish_bp = Blueprint('dish_bp', __name__)
@dish_bp.route('/api/v1/restaurants/<int:rid>/dishes', methods=['POST'])
def add_dish(rid):
    data = request.get_json()
    dish={
        "id":len(dishes)+1,
        "name":data["name"],
        "type":data["type"],
        "price":data["price"],
        "available_time":data["available_time"],
        "image":data.get("image"),
        "enabled":True
    }
    dishes.append(dish)
    return jsonify(dish),201
@dish_bp.route("/api/v1/dishes/<int:did>", methods=["PUT"])
def update_dish(did):
    data = request.get_json()
    for dish in dishes:
        if dish["id"]==did:
            dish.update(data)
            return jsonify(dish),200
    return jsonify({"error": "Dish not found"}), 404
@dish_bp.route("/api/v1/dishes/<int:did>/status", methods=["PUT"])
def update_dish_status(did):
    data = request.get_json()
    for dish in dishes:
        if dish["id"]==did:
            dish["enabled"]=data["enabled"]
            return jsonify({"message": "Status updated"})
    return jsonify({"error": "Dish not found"}), 404
@dish_bp.route("/api/v1/dishes/<int:did>", methods=["DELETE"])
def delete_dish(did):
    for dish in dishes:
        if dish["id"]==did:
            dishes.remove(dish)
            return jsonify({"message": "Dish deleted"})
    return jsonify({"error": "Dish not found"}), 404